from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_registration = KeyboardButton("Определить магазин")
button_case_registration = ReplyKeyboardMarkup(resize_keyboard=True).add(button_registration)



class FSMAdmin(StatesGroup):#Клас необходим для перехода между состояниями
    mag = State()
    last_number = State()



async def command_registration_user(message : types.Message):
    await message.answer("Ссылочки", reply_markup=button_case_registration)
    print('777')



def register_handlers_client(dp:Dispatcher):
    dp.register_message_handler(command_registration_user, commands=['start'])