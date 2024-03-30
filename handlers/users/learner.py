from keyboards.inline import keyboard, yonalish_nomi_keyboard, response_keyboard, uzbekistan_viloyatlar
from keyboards.inline import inline_tumanlar
from aiogram.dispatcher import FSMContext
from states.button import Learning
from aiogram import types
from uuid import uuid4
from loader import dp

list_ = ["Maktabgacha ta’lim tashkiloti tarbiyachisi", "Maktabgacha ta’lim tashkiloti psixologi",
         "Maktabgacha ta’lim tashkiloti direktori", "Maktabgacha ta’lim tashkiloti metodisti",
         "Maktabgacha ta’lim tashkiloti defektologi/logopedi", "Maktabgacha ta’lim tashkiloti musiqa rahbari",
         "Maktabgacha ta’lim tashkiloti oshpazi"]


@dp.callback_query_handler(lambda call: call.data == "registration", state='*')
async def answer_regitration(call: types.CallbackQuery):
    await call.message.answer("Telegram raqamingizni yuboring.", reply_markup=keyboard)
    await Learning.zero.set()


@dp.message_handler(content_types=types.ContentTypes.CONTACT, state=Learning.zero)
async def answer_contact(message: types.Message, state: FSMContext):
    await state.update_data({"Contact": message.contact.phone_number})
    await message.answer("Familiya, Ism va sharifingizni kiriting.")
    await Learning.next()


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Learning.one)
async def answer_name(message: types.Message, state: FSMContext):
    await state.update_data({"Name": message.text})
    await message.answer("Passportingiz seria va raqamini kiriting?!\n(Namuna: AD1010203)")
    await Learning.next()


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Learning.two)
async def answer_seria(message: types.Message, state: FSMContext):
    await state.update_data({"passport": message.text})
    await message.answer("Viloyatingizni tanglang.", reply_markup=uzbekistan_viloyatlar)
    await Learning.next()


@dp.callback_query_handler(state=Learning.three)
async def answer_viloyat(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"region": call.data})
    await call.message.answer("Tumaningizni tanlang.", reply_markup=await inline_tumanlar(call.data))
    await Learning.next()


@dp.callback_query_handler(state=Learning.four)
async def answer_tuman(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"tuman": call.data})
    await call.message.answer("Oliy yoki o'rta maxsus mutaxassislik diplomingiz rasmini yuklang")
    await Learning.next()


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Learning.five)
async def answer_passport(message: types.Message, state: FSMContext):
    photo = message.photo[-1]
    file_id = photo.file_id
    print(file_id)
    async with state.proxy() as data:
        data["diploma_photo"] = file_id

    await photo.
    await state.update_data({"address": message.text})
    await message.answer("Malaka oshirish kurslari toifalarini tanlang.", reply_markup=yonalish_nomi_keyboard)
    await Learning.next()


@dp.callback_query_handler(state=Learning.six)
async def answer_yonalish(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"yonalish": call.data})
    data = await state.get_data()
    data1 = (f"F. I. SH: {data.get('Name')}\nPassport: {data.get('passport')}\nViloyat: {data.get('region')}\nTuman: "
             f"{data.get('tuman')}\nManzil: {data.get('address')}\nYonalish: {list_[int(data.get('yonalish'))]}")
    await call.message.answer("Quyidagi kiritgan ma'lumotlaringiz to'g'ri ekanligini tasdiqlaysizmi?")
    await call.message.answer(text=data1, reply_markup=response_keyboard)
    await Learning.next()


@dp.callback_query_handler(state=Learning.seven)
async def answer_tasdiqlash(call: types.CallbackQuery, state: FSMContext):
    if call.data == "yes":
        await call.message.answer(
            text="✅ Ma'lumotlaringiz muvaffaqiyatli qabul qilindi. Sizni MTT da ko'rganimizdan xursandmiz!!! Guruh shaklanishi bilan sizga ushbu bot orqali guruh linki yuboriladi.")
        await Learning.next()
    elif call.data == "no":
        await call.message.answer(
            text="❌ Ma'lumotlaringiz qabul qilinmadi. Iltimos qaytadan urinib ko'ring!\nFamiliya, Ism va sharifingizni kiriting.")
        data = await state.get_data()
        await state.update_data({"Contact": data.get("Contact")})
        await Learning.zero.set()
# oliy yoki orta maxsus diplomingiz rasmini yuklaydi
# viloyat tuman
