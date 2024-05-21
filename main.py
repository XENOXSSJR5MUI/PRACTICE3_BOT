from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keboard.keyboards import get_keyboard_1, get_keyboard_2

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
    await message.answer('Здраствуйте, я вертуальный бот :) ', reply_markup= get_keyboard_1())

@dp.message_handler(lambda massage: massage.text == 'Отправь фото DragonBall')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://seeklogo.com/images/G/goku-symbol-logo-C3157507EA-seeklogo.com.png?v=638372782130000000', caption= "Dragon Ball!")

@dp.message_handler(lambda massage: massage.text == 'Перейти на след.клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить отправить фото BlackClover', reply_markup= get_keyboard_2())



@dp.message_handler(lambda massage: massage.text == 'Отправь фото BlackClover')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://logowik.com/content/uploads/images/black-clover8928.jpg', caption= "Black Clover!")

@dp.message_handler(lambda massage: massage.text == 'Перейти на след.клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить отправить фото DragonBall', reply_markup= get_keyboard_1())


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