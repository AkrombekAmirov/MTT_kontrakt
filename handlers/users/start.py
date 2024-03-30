from keyboards.inline import keyboard, choose_visitor
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message, ContentType
from aiogram.dispatcher import FSMContext
from data.config import ADMIN, ADMIN1
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    await message.answer("Xizmat turini tanlang", reply_markup=choose_visitor)
