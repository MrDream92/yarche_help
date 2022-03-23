"""from aiogram import Bot, Dispatcher, executor, types
from config import *

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello! Im Gunther Bot, Please follow my YT channel")

@dp.message_handler(commands=['logo'])
async def logo(message: types.Message):
    await message.answer_photo('https://avatars.githubusercontent.com/u/62240649?v=4')

@dp.message_handler()
async def echo(message: types.Message):
    text = f"Привет, ты написал: {message.text}"
    await message.reply(text=text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)"""

import logging

from aiogram import Bot, Dispatcher, executor, types

# Токен, выданный BotFather в телеграмме
API_TOKEN = "5182616067:AAEPUM-mkz1Ier0a4J7DyykHsSfeb1bTIMU"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)