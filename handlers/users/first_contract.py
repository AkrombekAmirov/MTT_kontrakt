from keyboards.inline import rasmiylashtirish, uzbekistan_viloyatlar, talim_shakli_keyboard, choose_language, \
    yonalish_nomi_keyboard, response_keyboard, choose_status
from utils.main.repository import file_create, get_file_user
from file_service.first_stage import check_passport1
from file_service.wr_code_core import func_qrcode
from file_service.file_path import get_file_path
from file_service.dictionary import kunduzgi
from keyboards.inline import choose_visitor
from aiogram.dispatcher import FSMContext
from file_service.core import file_send
from states.button import Visitor
from .anketa import handle_func
from aiogram import types
from uuid import uuid4
from loader import dp


@dp.callback_query_handler(lambda call: call.data == "abituriyent", state='*')
async def answer_contract(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Xizmat turini tanlang", reply_markup=choose_visitor)


@dp.callback_query_handler(lambda call: call.data in ["registration"])
async def answer_registration(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Passportingiz seria va raqamini kiriting?!\n(Namuna: AA1234567)")
    await Visitor.one.set()


@dp.message_handler(state=Visitor.one)
async def answer_passport(message: types.Message, state: FSMContext):
    await state.update_data({"passport": message.text})
    await message.answer("JSHSHIR kiriting")
    await Visitor.next()


@dp.message_handler(state=Visitor.two)
async def answer_jshshir(message: types.Message, state: FSMContext):
    await state.update_data({"JSHSHIR": message.text})
    await message.answer("Viloyatingizni tanlang", reply_markup=uzbekistan_viloyatlar)
    await Visitor.next()


@dp.callback_query_handler(state=Visitor.three)
async def answer_viloyat(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"region": call.data})
    await call.message.answer("Yashash manzilingizni kiriting. 📍")
    await Visitor.next()


@dp.message_handler(state=Visitor.four)
async def answer_manzil(message: types.Message, state: FSMContext):
    await state.update_data({"address": message.text})
    await message.answer("Siz qaysi ta'lim shakli buyicha o'qishingizni tanlang!", reply_markup=talim_shakli_keyboard)
    await Visitor.next()


@dp.callback_query_handler(state=Visitor.five)
async def answer_talim_shakli(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"talim_shakli": call.data})
    await call.message.answer("Ta'lim tilini tanlang", reply_markup=choose_language)
    await Visitor.next()


@dp.callback_query_handler(state=Visitor.six)
async def answer_talim_tili(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"talim_tili": call.data})
    await call.message.answer("Yo'nalish nomini tanlang", reply_markup=yonalish_nomi_keyboard)
    await Visitor.next()


@dp.callback_query_handler(state=Visitor.seven)
async def answer_talim_tili(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"yonalish": call.data})
    data = await state.get_data()
    data1 = f"Passport seria va raqam: <b>{data.get('passport')}</b>\nJSHSHIR: <b>{data.get('JSHSHIR')}</b>\nViloyat: <b>{data.get('region')}</b>\nManzilingiz: <b>{data.get('address')}</b>\nTa'lim shakli: <b>{data.get('talim_shakli')}</b>\nTa'lim tili: <b>{data.get('talim_tili')}</b>\nTa'lim yo'nalishi:<b> {kunduzgi[data.get('yonalish')]['nomi']}</b>"
    await call.message.answer(f"Quyidagi kiritgan ma'lumotlaringiz to'g'ri ekanligini tasdiqlaysizmi?")
    await call.message.answer(text=data1, reply_markup=response_keyboard, allow_sending_without_reply=True,
                              protect_content=True, parse_mode="HTML")
    await Visitor.next()


@dp.callback_query_handler(state=Visitor.eight)
async def answer_talim_tili(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"response": call.data})
    data = await state.get_data()
    if data.get("response") == "1":
        await call.message.answer(
            "✅ Ma'lumotlaringiz muvaffaqiyatli qabul qilindi. \nMehnat va ijtimoiy munosabatlar akademiyasini tanlaganiz uchun raxmat!!!",
            reply_markup=choose_status)
        await state.finish()
        await state.reset_state()
    else:
        await state.finish()
        await state.reset_state()
        await call.message.answer("Passportingiz seria va raqamini kiriting?!\n(Namuna: AA1234567)")
        await Visitor.one.set()
