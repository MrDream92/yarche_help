from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from create_bot import bot, dp

button_registration = KeyboardButton("Определить магазин")
button_case_registration = ReplyKeyboardMarkup(resize_keyboard=True).add(button_registration)



class FSMAdmin(StatesGroup):#Клас необходим для перехода между состояниями
    mag = State()
    last_number = State()


"""async def start_user(message : types.Message):
    await bot.send_message(message.from_user.id, )"""



async def command_registration_user(message : types.Message):
    await bot.send_message(message.from_user.id, "Введите номер магазина в формате Т001, Н002, М003..." , reply_markup=button_case_registration)
    await FSMAdmin.mag.set()
    #await message.delete()


async def set_last_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mag'] = message.text
    await FSMAdmin.next()
    await message.reply("Теперь введите последние 4 цифры номера телефона")


async def load_data_registration(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_number'] = float(message.text)

    async with state.proxy() as data:
       await message.reply(str(data))#а вот и данные что мы навводили

    #Тут запрос к БД

    await state.finish()




async def echo(message: types.Message):
    await message.answer(message.text)


def register_handlers_client(dp:Dispatcher):
    #dp.register_message_handler(start_user, commands=['start'])
    dp.register_message_handler(command_registration_user, commands=['registration'], state=None)
    dp.register_message_handler(set_last_number, state=FSMAdmin.mag)
    dp.register_message_handler(load_data_registration, state=FSMAdmin.last_number)
    dp.register_message_handler(echo)


