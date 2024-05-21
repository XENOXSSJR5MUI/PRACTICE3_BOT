from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description= 'Команда для того, чтобы запустить бота'),
        types.BotCommand(command='/help', description= 'Команда помощи при работе с ботом')
    ]
    await bot.set_my_commands(commands)




@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Здраствуйте, я вертуальный бот :) ')

@dp.message_handler(commands= 'help')
async def help(message: types.Message):
    await message.reply('Чем вам помочь? ')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def on_startup(dispacher):
    await set_commands(dispacher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)