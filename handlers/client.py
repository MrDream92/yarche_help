from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from create_bot import bot, dp

button_registration = KeyboardButton("/Определить магазин")
button_case_registration = ReplyKeyboardMarkup(resize_keyboard=True).add(button_registration)

mags = ["М001", "М002", "М003"]


class FSM_user(StatesGroup):#Клас необходим для перехода между состояниями
    number_user = State()
    mag_user = State()


async def registration_start(message: types.Message):
    await message.answer("Введите ваш номер телефона:")
    await FSM_user.number_user.set()





async def echo(message: types.Message):
    await message.answer(message.text)


def register_handlers_client(dp:Dispatcher):
    dp.register_message_handler(registration_start, commands='start', state="*")
    dp.register_message_handler(echo)


