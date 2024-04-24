from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline import choose_visitor
from aiogram.types import Message
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    await message.answer("Xizmat turini tanlang", reply_markup=choose_visitor)
