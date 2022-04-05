from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from create_bot import bot, dp, BD_URI

import psycopg2

db_connection = psycopg2.connect(BD_URI, sslmode='require')
db_object = db_connection.cursor()



class FSM_user(StatesGroup):#Клас необходим для перехода между состояниями
    number_user = State()
    mag_user = State()


async def set_user_number(message: types.Message, state: FSMContext):
    #Необходимо проверить есть ли уже завязанный магазин на пользователе
    db_object.execute('SELECT * FROM users WHERE user_id = %s', (str(message.from_user.id),))
    result = db_object.fetchone()

    print(result)

    if not result:
        await message.answer(text='Введите  ваш номер телефона в формате 8911111111')
        await FSM_user.number_user.set()
    else:
        #await message.answer(f'К вам уже привязан магазин %s',(result))
        await message.answer(result)

async def set_mag_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number_user'] = message.text
    await FSM_user.next()

    mags = list()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    db_object.execute('SELECT * FROM users WHERE user_number = %s', (str(message.text),))
    result = db_object.fetchall()
    if not result:
        await message.answer(text='По данному номеру нет зарегистрированных магазинов... Обратитесь к администратору')
        await state.finish()
    else:

        for item in enumerate(result):

            mags.append(item[1][3])

    for size in mags:
        keyboard.add(size)
    await message.answer("Вам доступны следующие магазины:", reply_markup=keyboard)


async def final_data_FSM(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mag_user'] = message.text

    #async with state.proxy() as data:
    #   await message.reply(str(data))#а вот и данные что мы навводили

    async with state.proxy() as data:
        #    cur.execute('INSERT INTO menu VALUES(?,?,?,?)', tuple(data.values()))
        #   base.commit()
            #await message.reply(tuple(data.values()))
        #print(message.from_user.id)
        #print(data['number_user'])
        #print(data['mag_user'])

        query = "Update users set user_id = %s where user_number = %s and mag_number = %s"
        db_object.execute(query, (message.from_user.id, data['number_user'],data['mag_user']))
        db_connection.commit()

        await message.reply(f"Магазин {data['mag_user']} зарегистрирован за вами!")

    await state.finish()
    #await message.reply("Я записал это в базу данных")


async def echo(message: types.Message):
    await message.answer(message.text)



def register_handlers_client(dp:Dispatcher):
    dp.register_message_handler(set_user_number, commands="start", state="*")
    dp.register_message_handler(set_mag_number, state=FSM_user.number_user, content_types=types.ContentTypes.TEXT)
    dp.register_message_handler(final_data_FSM, state=FSM_user.mag_user, content_types=types.ContentTypes.TEXT)

    dp.register_message_handler(echo)


