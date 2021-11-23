from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os, json, string

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот в сети')


"""**********************************************Клиент**********************************************"""


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного.')
        # await message.delete()
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему:\nhttps://t.me/ItsTimeToGetBetterBot")


"""**********************************************Админка**********************************************"""

"""**********************************************Общая часть******************************************"""


@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Цензура, ёба.')
        await message.delete()


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
