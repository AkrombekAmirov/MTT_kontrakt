from utils.main.repository import file_create, get_file_user, create_user_info, get_user_info
from file_service.generate_qrcode import create_new_qrcode, get_image
from file_service.core import file_send, file_send_invitation
from file_service.first_stage import check_passport1
from file_service.check_file import check_passport
from file_service.wr_code_core import func_qrcode
from file_service.file_path import get_file_path
from aiogram.dispatcher import FSMContext
from states.button import Personal
from keyboards.inline import *
from aiogram import types
from uuid import uuid4
from loader import dp


@dp.callback_query_handler(text='talaba', state="*")
async def answer_contact(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Telegram raqamingizni yuboring.",
                              reply_markup=keyboard)
    await Personal.Contact.set()


@dp.message_handler(content_types=types.ContentType.CONTACT, state=Personal.Contact)
async def answer_contact(message: types.Message, state: FSMContext):
    await state.update_data({"Contact": message.text})
    await message.answer("Kursingizni tanlang.", reply_markup=rasmiylashtirish)
    await Personal.next()


@dp.callback_query_handler(state=Personal.Stage)
async def answer_stage(call: types.CallbackQuery, state: FSMContext):
    if call.data == "registration":
        await state.finish()
        await state.reset_data()
        await call.message.answer("Xizmat turini tanlang", reply_markup=choose_status)

    else:
        await state.update_data({"Stage": call.data})
        await call.message.answer("Xizmat turini tanlang", reply_markup=contract_keyboard)
        await Personal.next()


@dp.callback_query_handler(state=Personal.Service)
async def answer_contract(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"Service": call.data})
    await call.message.answer("Pasportingiz seria va raqamlarini kiriting?!\n(Namuna: AA123456)")
    await Personal.next() if call.data in ["ikkitomonlama", "uch_tom"] else await Personal.Invitation.set()


@dp.message_handler(state=Personal.Invitation)
async def answer_seria(message: types.Message, state: FSMContext):
    await state.update_data({"Seria": message.text})
    await core_func(message=message, state=state, uuid=uuid4())


async def core_func(message, state, uuid):
    state_data = await state.get_data()
    data = await check_passport1(f"{state_data['Seria']}") if state_data[
                                                                  'Stage'] == "1" else await check_passport(
        f"{state_data['Seria']}")
    print(data, state_data['Seria'], "Chaqiruv xati")
    info = await get_user_info(user_id=f"{state_data['Seria']}")
    if data is None:
        await message.answer("Malumot topilmadi! Iltimos qaytadan urinib ko'ring!")
        await func_reset_state(state_data=state_data, state=state, message=message)
    elif state_data['Stage'] == '1':
        await message.answer("Birinchi kurslarga ruxsat etilmagan!")
        await func_reset_state(state_data=state_data, state=state, message=message)
    elif data[6] == 'Kunduzgi':
        await message.answer("Kunduzgi ta'lim uchun ruhsat etilmagan!")
        await func_reset_state(state_data=state_data, state=state, message=message)
    # elif info:
    #     if info.phone_number:
    #         await message.answer("Telefon raqami avval olingan!")
    #         await func_reset_state(state_data=state_data, state=state, message=message)
    elif bool(await get_file_user(user_id=f"{state_data['Seria']}", contract_type='FileRepositoryCh')) is True:
        # await message.answer("Bu pasport seria bilan malumot avval olingan. Passport seria raqamini kiriting!!!")
        await message.answer("Ma'lumotnoma rasmiylashtirilmoqda. Biroz kuting.")
        await message.answer_document(types.InputFile(await get_file_path(name=f'Invitation_file\\{data[1]}.pdf')))
        await func_reset_state(state_data=state_data, state=state, message=message)

    elif await get_user_info(user_id=f"{state_data['Seria']}") is None:
        print('birinchi if')
        func_qrcode(url=uuid, name=f"Inv{data[1]}", path_='Inv')
        num = await file_send_invitation(data=data)
        await message.answer("Ma'lumotnoma rasmiylashtirilmoqda. Biroz kuting.")
        await create_user_info(user_id=f"{state_data['Seria']}", name=data[1], telegram_id=message.from_user.id,
                               telegram_name=message.from_user.username if message.from_user.username else 'None',
                               phone_number=state_data['Contact'],
                               faculty=data[5], group=data[8], stage=state_data['Stage'], shakli=data[6])
        with open(await get_file_path(name=f'Invitation_file\\{data[1]}.pdf'), 'rb') as file:
            await file_create(contract_type='FileRepositoryCh', user_id=[f"{state_data['Seria']}", uuid, num],
                              images=[(file, "application/pdf")])
        await message.answer_document(types.InputFile(await get_file_path(name=f'Invitation_file\\{data[1]}.pdf')))
        await func_reset_state(state_data=state_data, state=state, message=message)
    # elif bool(await get_file_user(user_id=f"{state_data['Seria']}", contract_type='FileRepositoryCh')) is False or await get_user_info(user_id=f"{state_data['Seria']}") is False:
    #     print('ishladi')
    #     await message.answer("Ma'lumotnoma rasmiylashtirilmoqda. Biroz kuting")
    #     func_qrcode(url=uuid, name=f"Inv{data[1]}", path_='Inv')
    #     num = await file_send_invitation(data=data)
    #     with open(await get_file_path(name=f'Invitation_file\\{data[1]}.pdf'), 'rb') as file:
    #         await file_create(contract_type='FileRepositoryCh', user_id=[f"{state_data['Seria']}", uuid, num],
    #                           images=[(file, "application/pdf")])
    #     await message.answer_document(types.InputFile(await get_file_path(name=f'Invitation_file\\{data[1]}.pdf')))
    #     await func_reset_state(state_data=state_data, state=state, message=message)


@dp.message_handler(state=Personal.Contract)
async def answer_check(message: types.Message, state: FSMContext):
    await state.update_data({"Seria": message.text})
    data = await state.get_data()
    func_data = await check_passport1(f"{data['Seria']}") if data[
                                                                 'Stage'] == "1" else await check_passport(
        f"{data['Seria']}")
    # func_data = await check_passport(f"{data['Seria']}")
    print(func_data, message.text)
    file_uuid = uuid4()
    if func_data is None:
        await handle_func(message, state, "Ma'lumot topilmadi. Qaytadan boshqa passport seria kiriting!!!",
                          state_data=data)
    # elif data['Stage'] == '1':
    #     await handle_func(message, state,
    #                       "Birinchi kurslarga shartnoma berish muddati tagatildi!!!",
    #                       state_data=data)

    elif bool(await get_file_user(user_id=f"{func_data[3]}", contract_type='FileRepository')) is True:
        print(func_data[1])
        data0 = await get_image(name=str(func_data[1]))
        print(data0)
        await create_new_qrcode(url=data0, name=str(func_data[1]))
        with open(await get_file_path(name=f'new_qrcode/{func_data[1]}.png'), 'rb') as file:
            input = types.InputFile(await get_file_path(name=f'new_qrcode/{func_data[1]}.png'))
            await message.reply_photo(input)
        await handle_func(message, state,
                          "Bu pasport seria bilan shartnoma avval olingan. Yuqoridagi qr kodni skanerlash orqali shartnomani qaytadan yuklab oling!!!",
                          state_data=data)

    elif func_data is None:
        await handle_func(message, state,
                          "Bu pasport seria bilan shartnoma avval olingan yoki tizimda mavjud bo'lmagan pasport seria kiritdingiz!!!. Qaytadan boshqa pasport seria kiriting!!!\nNamuna: AB123456",
                          state_data=func_data)

    elif bool(func_data) is True:
        func_data.append(data["Service"])
        await handle_valid_passport(message, state, func_data, file_uuid, data)


async def handle_func(message, state, text, state_data):
    await message.answer(text)
    await finish_and_reset_state(message, state, state_data=state_data)


async def handle_valid_passport(message, state, func_data, file_uuid, data):
    func_qrcode(url=file_uuid, name=func_data[1], path_=None)
    await message.answer("Shartnoma rasmiylashtirilmoqda. Biroz kuting.")
    name = await file_send(func_data)
    print(name)
    with open(await get_file_path(name=f"file/{name[0]}{func_data[1]}.pdf"), "rb") as file:
        await file_create(contract_type='FileRepository', user_id=[f"{func_data[3]}", file_uuid, name[1]],
                          images=[(file, "application/pdf")])
        input_file = types.InputFile(await get_file_path(name=f"file/{name[0]}{func_data[1]}.pdf"))
        await message.answer_document(input_file)

    await finish_and_reset_state(state_data=data, state=state, message=message)


async def finish_and_reset_state(message, state, state_data):
    await state.finish()
    await state.reset_state()
    await Personal.Stage.set()
    await state.update_data({'Contact': state_data['Contact']})
    await message.answer("Akademiya intraktiv xizmatlari botidan foydalanish uchun kursingizni tanlang!!!",
                         reply_markup=rasmiylashtirish)


async def func_reset_state(state_data, state, message):
    await state.reset_state()
    await Personal.Stage.set()
    await state.update_data({'Contact': state_data['Contact']})
    await message.answer("Akademiya intraktiv xizmatlari botidan foydalanish uchun kursingizni tanlang!!!",
                         reply_markup=rasmiylashtirish)
