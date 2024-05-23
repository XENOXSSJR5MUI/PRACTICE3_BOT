from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keboard.keyboards import get_keyboard_1, get_keyboard_2
from keboard.key_inline import get_keyboard_inline

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

@dp.message_handler(lambda message: message.text == 'Отправь фото DragonBall')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://seeklogo.com/images/G/goku-symbol-logo-C3157507EA-seeklogo.com.png?v=638372782130000000', caption= "Dragon Ball!", reply_markup= get_keyboard_inline())

@dp.message_handler(lambda message: message.text == 'Перейти на след.клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить отправить фото BlackClover', reply_markup= get_keyboard_2())



@dp.message_handler(lambda message: message.text == 'Отправь фото BlackClover')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://logowik.com/content/uploads/images/black-clover8928.jpg', caption= "Black Clover!")

@dp.message_handler(lambda message: message.text == 'Вернуться на 1 клавиатуру')
async def button_4_click(message: types.Message):
    await message.answer('Тут ты можешь попросить отправить фото BlackClover', reply_markup= get_keyboard_1())

@dp.message_handler(commands= 'help')
async def help(message: types.Message):
    await message.reply('Чем вам помочь?')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def on_startup(dispacher):
    await set_commands(dispacher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)