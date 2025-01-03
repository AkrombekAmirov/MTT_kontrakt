from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline import choose_visitor, admin_keyboard
from aiogram.types import Message
from loader import dp
from data.config import ADMIN_M1, ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    if str(message.from_user.id) == str(ADMIN_M1) or str(message.from_user.id) == str(ADMINS):
        await message.answer("Xizmat turini tanlang", reply_markup=admin_keyboard)
    else:
        await message.answer("Xizmat turini tanlang", reply_markup=choose_visitor)
