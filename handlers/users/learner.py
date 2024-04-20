from keyboards.inline import keyboard, yonalish_nomi_keyboard, response_keyboard, uzbekistan_viloyatlar, choose_visitor, \
    choose_contract_, seria_keyboard, number_keyboard, list_regioin, list_tuman, list_region1
from file_service.file_read import process_document, process_contract, func_qrcode, write_qabul
from file_service.file_path import get_file_path
from keyboards.inline import inline_tumanlar
from aiogram.dispatcher import FSMContext
from utils.db_api.postgresql1 import *
from states.button import Learning
from datetime import datetime
from aiogram import types
from uuid import uuid4
from loader import dp
import logging
import re
from os.path import join, dirname

logging.basicConfig(filename='bot.log', filemode='w', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

list_ = ["Maktabgacha ta’lim tashkiloti tarbiyachisi", "Maktabgacha ta’lim tashkiloti psixologi",
         "Maktabgacha ta’lim tashkiloti direktori", "Maktabgacha ta’lim tashkiloti metodisti",
         "Maktabgacha ta’lim tashkiloti defektologi/logopedi", "Maktabgacha ta’lim tashkiloti musiqa rahbari",
         "Maktabgacha ta’lim tashkiloti oshpazi"]


@dp.message_handler(commands=['start'])
async def exit_system(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=True)  # Holatni tozalash
    await message.answer("Xizmat turini tanlang", reply_markup=choose_visitor)


@dp.callback_query_handler(lambda call: call.data == "registration", state='*')
async def answer_regitration(call: types.CallbackQuery):
    print(call.data)
    logging.info(f"{call.from_user.id} {call.from_user.full_name} {call.data}")
    await call.message.answer("Telegram raqamingizni yuboring.", reply_markup=keyboard)
    await Learning.zero.set()


@dp.message_handler(content_types=types.ContentTypes.ANY, state=Learning.zero)
async def answer_contact(message: types.Message, state: FSMContext):
    if message.text == '/start':
        await exit_system(message, state)
    elif message.contact:
        logging.info(f"{message.from_user.id} {message.from_user.full_name} {message.contact.phone_number}")
        await state.update_data({"Contact": message.contact.phone_number})
        await message.answer("Familiya, Ism va Sharifingizni kiriting.")
        await Learning.next()
    else:
        await message.answer("Iltimos telegram kontaktingizni yuboring!")
        await Learning.zero.set()


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Learning.one)
async def answer_name(message: types.Message, state: FSMContext):
    logging.info(f"{message.from_user.id} {message.from_user.full_name} {message.text}")
    await message.delete()
    if message.text.startswith("/start"):
        await exit_system(message, state)
    elif re.match(r"^[A-Za-z\s']+$", message.text):
        await state.update_data({"Name": message.text})
        await message.answer("Passportingiz seria va raqamini kiriting!", reply_markup=seria_keyboard)
        await Learning.next()
    else:
        await message.answer(
            "Siz malumot kiritishda xatolikga yo'l quydingiz! Iltimos Familiya, Ism va Sharifingizni  lotin alifbosida kiriting.")
        await Learning.one.set()


@dp.callback_query_handler(lambda call: call.data in ["AA", "AB", "AC", "AD", "AE", "KA"], state=Learning.two)
async def answer_seria(call: types.CallbackQuery, state: FSMContext):
    logging.info(f"{call.from_user.id} {call.message.from_user.full_name} {call.data}")
    await state.update_data({"passport_seria": call.data})
    await call.message.delete()
    await call.message.answer(f"Passportingiz  seriasini kiriting: {call.data}", reply_markup=number_keyboard)
    await Learning.next()


@dp.callback_query_handler(lambda call: call.data in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "number_back"],
                           state=Learning.three)
async def answer_seria(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    logging.info(f"{call.from_user.id} {call.message.from_user.full_name} {call.data} {data.get('passport_number')}")
    if str(call.data) == "number_back" and len(str(data.get("passport_number"))) != 0:
        await state.update_data({"passport_number": f"{data.get('passport_number')[:-1]}"})
    elif str(data.get("passport_number"))[0:4] == "None":
        await state.update_data({"passport_number": call.data})
    elif str(call.data) != "number_back":
        await state.update_data({"passport_number": f"{data.get('passport_number')}{call.data}"})
    data = await state.get_data()
    if len(str(data.get("passport_number"))) == 7:
        print(data.get("passport_seria"), data.get("passport_number"))
        if get_user_info(passport=f"{data.get('passport_seria')}{data.get('passport_number')}"):
            await call.message.answer(
                "Bu passport seriyasi va raqami bilan avval ro'yxatdan o'tgan. Iltimos qaytadan urinib ko'ring!",
                reply_markup=choose_visitor)
            await state.reset_state(with_data=True)
        else:
            await state.update_data({"passport": data.get("passport_seria") + data.get("passport_number")})
            await call.message.delete()
            await call.message.answer("Viloyatingizni tanglang.", reply_markup=uzbekistan_viloyatlar)
            await Learning.four.set()
    else:
        await call.message.edit_text(
            f"Passport raqamini kiriting: {data.get('passport_seria')} {data.get('passport_number')}",
            reply_markup=number_keyboard)


@dp.callback_query_handler(lambda call: call.data in list_regioin, state=Learning.four)
async def answer_viloyat(call: types.CallbackQuery, state: FSMContext):
    logging.info(f"{call.from_user.id} {call.message.from_user.full_name} {call.data}")
    await call.message.delete()
    print(call.data)
    print(list_region1[int(call.data[3:])])
    await state.update_data({"region": list_region1[int(call.data[3:])]})
    await call.message.answer("Tumaningizni tanlang.", reply_markup=await inline_tumanlar(call.data))
    await Learning.next()


@dp.callback_query_handler(lambda call: call.data in list_tuman, state=Learning.five)
async def answer_tuman(call: types.CallbackQuery, state: FSMContext):
    logging.info(f"{call.from_user.id} {call.message.from_user.full_name} {call.data}")
    await call.message.delete()
    await state.update_data({"tuman": call.data})
    await call.message.answer("Malaka oshirish kurslari yo'nalishini tanlang.", reply_markup=yonalish_nomi_keyboard)
    await Learning.next()


@dp.callback_query_handler(
    lambda call: call.data in ["faculty0", "faculty1", "faculty2", "faculty3", "faculty4", "faculty5", "faculty6"],
    state=Learning.six)
async def answer_five(call: types.CallbackQuery, state: FSMContext):
    logging.info(f"{call.from_user.id} {call.message.from_user.full_name} {call.data}")
    await state.update_data({"yonalish": call.data})
    await call.message.delete()
    data = await state.get_data()
    data1 = (
        f"Quyidagi kiritgan ma'lumotlaringiz to'g'ri ekanligini tasdiqlaysizmi?\nF. I. SH: {data.get('Name')}\nPassport: <b>{data.get('passport')}</b>\nViloyat: {data.get('region')}\nTuman: "
        f"{data.get('tuman')}\nYonalish: {list_[int(data.get('yonalish')[7])]}")
    await call.message.answer(text=data1, reply_markup=response_keyboard)
    await Learning.next()


@dp.callback_query_handler(state=Learning.seven)
async def answer_regitration(call: types.CallbackQuery, state: FSMContext):
    if call.data == "yes":
        await call.message.answer("✅ Ma'lumotlaringiz muvaffaqiyatli qabul qilindi.\n")
        response = await call.message.answer_document(
            types.InputFile(await get_file_path(name="shartnoma_.pdf")),
            caption="Shartnoma bilan tanishib chiqing!!!")
        await call.message.answer(
            "Malaka oshirish kurslarida o'qish uchun yuqoridagi shartnoma bilan tanishib chiqing va shartnoma qoidalari sizni qanoatlantirsa quyidagi tugmani bosing va ariza qoldiring!!!",
            reply_markup=choose_contract_)
        print(response.document.file_id)
        await Learning.next()
    elif call.data == "no":
        await call.message.answer(
            "❌ Ma'lumotlaringiz qabul qilinmadi.\nIltimos qaytadan urinib ko'ring!\nFamiliya, Ism va Sharifingizni kiriting.")
        data = await state.get_data()
        await state.reset_state(with_data=True)
        await state.update_data({"Contact": data.get("Contact")})
        await Learning.one.set()
    elif call.data == "back_to_menu":
        await call.message.answer("Xizmat turini tanlang", reply_markup=choose_visitor)
        await state.reset_state(with_data=True)


@dp.callback_query_handler(state=Learning.eight)
async def answer_choose(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    if call.data == "qabul_yes":
        await call.message.answer(
            "✅ Sizning arizangiz qabul qilindi.\nShartnomangizni yuklab olish uchun pasportingiz seria raqamini kiriting!")
        await Learning.next()
    elif call.data == "inkor_no":
        await state.finish()
        await state.reset_state(with_data=True)
        await call.message.answer("Xizmat turini tanlang", reply_markup=choose_visitor)


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Learning.nine)
async def answer_passport_seria(message: types.Message, state: FSMContext):
    logging.info(f"{message.from_user.full_name} {message.text}")
    data = await state.get_data()
    print(data)
    info = message.text.upper().strip()
    print(info.strip())
    if len(info) == 9 and info[:2].isalpha() and info[2:].isdigit():
        if data.get('passport') == message.text:
            await message.answer("Shartnoma rasmiylashtirilmoqda. Biroz kuting.")
            await create_func(data, message)
            await message.answer(
                "✅ Shartnoma muvaffaqiyatli rasmiylashtirildi. Sizni ushbu kursda ko'rganimizdan mamnunmiz!!! Guruh shaklanishi bilan sizga ushbu bot orqali guruh linki yuboriladi.",
                reply_markup=choose_visitor)
            await state.reset_state(with_data=True)
        else:
            await message.answer("Passportingiz seria va raqami noto'g'ri kiritildi. Iltimos qaytadan urinib ko'ring!")
            await Learning.nine.set()
    else:
        await message.answer(
            "Ruxsat etilmagan belgilardan foydalandingiz. Iltimos qaytadan pasport seria va raqamni kiriting!")
        await Learning.nine.set()


async def create_func(data, message):
    uuid_id = str(uuid4())
    ariza_id = str(uuid4())
    contract_number = get_max_contract_number()
    data2 = [[data.get('Name'), data.get('passport'), contract_number, data.get('region'), data.get('tuman'),
              list_[int(data.get('yonalish')[7])], data.get('Contact'), datetime.now().strftime("%d-%m-%Y")]]
    await write_qabul(data=data2)
    await func_qrcode(url=uuid_id, name=f"{data.get('Name')}", status=True)
    await func_qrcode(url=ariza_id, name=f"{data.get('Name')}")
    await process_document(f"{data.get('region')} {data.get('tuman')}da", f"{data.get('Name')}")
    await process_contract(name=f"{data.get('Name')}", faculty=f"{list_[int(data.get('yonalish')[7])]}",
                           passport=f"{data.get('passport')}", number=f"{data.get('Contact')}",
                           address=f"{data.get('region')} {data.get('tuman')}",
                           contract_number=contract_number)
    response1 = await message.answer_document(
        types.InputFile(await get_file_path(name=f"file_ariza\\{data.get('Name')}.pdf")), caption="Sizning arizangiz")
    response = await message.answer_document(
        types.InputFile(await get_file_path(name=f"file_shartnoma\\{data.get('Name')}.pdf")),
        caption="Sizning arizangizga binoan siz bilan tuzilgan shartnoma")
    create_user_info(name=data.get("Name"), passport=data.get("passport"), telegram_id=message.from_user.id,
                     telegram_number=data.get("Contact"), contract_number=contract_number,
                     telegram_file_id=str(response.document.file_id), telegram_ariza_id=str(response1.document.file_id),
                     telegram_name=message.from_user.full_name,
                     username=message.from_user.username if message.from_user.username else "None", ariza_id=ariza_id,
                     file_id=uuid_id, faculty=list_[int(data.get("yonalish")[7])], group="001",
                     created_date=datetime.now().strftime("%Y-%m-%d"), created_time=datetime.now().strftime("%H:%M:%S"))
    with open(await get_file_path(name=f"file_shartnoma\\{data.get('Name')}.pdf"), "rb") as file:
        await file_create_(user_id=[f"{data.get('passport')}", uuid_id, contract_number],
                           images=[(file, "application/pdf")])
    with open(await get_file_path(name=f"file_ariza\\{data.get('Name')}.pdf"), "rb") as file:
        await file_create_(user_id=[f"{data.get('passport')}", ariza_id, contract_number],
                           images=[(file, "application/pdf")])
    with open(await get_file_path(name=f"qabul.xlsx"), "rb") as file:
        await dp.bot.send_document(chat_id=["1827964433", "1709066039"], document=file)
    await dp.bot.send_document(chat_id=["1827964433", "1709066039"], document=response.document.file_id)
    await dp.bot.send_document(chat_id=["1827964433", "1709066039"], document=response1.document.file_id)

