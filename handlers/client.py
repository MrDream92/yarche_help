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


class reg(StatesGroup):
    name = State()
    fname = State()
    age = State()


#@dp.message_handler(commands="reg", state="*")
async def name_step(message: types.Message, state: FSMContext):
    await message.answer(text='Напиши имя ')
    await reg.name.set()


#@dp.message_handler(state=reg.name, content_types=types.ContentTypes.TEXT)
async def fname_step(message: types.Message, state: FSMContext):
    if any(map(str.isdigit, message.text)):
        await message.reply("Пожалуйста напишите свое имя")
        return
    await state.update_data(name_user=message.text.title())
    await message.answer(text='Напиши фамилию ')
    await reg.fname.set()


#@dp.message_handler(state=reg.fname, content_types=types.ContentTypes.TEXT)
async def age_step(message: types.Message, state: FSMContext):
    if any(map(str.isdigit, message.text)):
        await message.reply("Пожалуйста напишите свою фамилию")
        return
    await message.answer(text='Напиши возраст ')
    await state.update_data(fname_user=message.text.title())
    await reg.age.set()


async def echo(message: types.Message):
    await message.answer(message.text)


def register_handlers_client(dp:Dispatcher):
    #dp.register_message_handler(registration_start, commands='start', state="*")
    dp.register_message_handler(name_step, commands="reg", state="*")
    dp.register_message_handler(fname_step, state=reg.name, content_types=types.ContentTypes.TEXT)
    dp.register_message_handler(age_step, state=reg.fname, content_types=types.ContentTypes.TEXT)

    dp.register_message_handler(echo)


