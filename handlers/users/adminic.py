from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from states.button import Adminic
from utils.db_api.postgresql1 import delete_user, get_user_passport_id
from keyboards.inline.keyboards_inline import admin_keyboard, admin_response

@dp.callback_query_handler(lambda call: call.data == "delete_user")
async def adminic(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Foydalanuvchini o'chirish uchun pasport seria va raqamini kiriting!\nNamuna: AA1234567")

@dp.message_handler(types.Message)
async def adminic(message: types.Message, state: FSMContext):
    if not get_user_passport_id(message.text):
        await message.answer("Bunday foydalanuvchi topilmadi!", reply_markup=admin_keyboard)
    elif get_user_passport_id(message.text):
        user = get_user_passport_id(message.text)
        print(user.name, user.faculty, user.contract_number)
        await message.answer(f"F.I.Sh:{user.name}\n"
                             f"Yonalish: {user.faculty}\n"
                             f"Contract number: {user.contract_number}\n"
                             f"Raqam: {user.telegram_number}\n"
                             f"Passport: {user.passport}\nRostan o'chirasizmi?", reply_markup=admin_response)

@dp.callback_query_handler(lambda call: call.data in ["admin_yes", "admin_no"])
async def adminic(call: types.CallbackQuery, state: FSMContext):
    if call.data == "admin_yes":
        delete_user(call.from_user.id)
        await call.message.answer("Foydalanuvchi o'chirildi!", reply_markup=admin_keyboard)
    elif call.data == "admin_no":
        await call.message.answer("Foydalanuvchi o'chirilmadi!", reply_markup=admin_keyboard)
    await state.reset_state(with_data=True)