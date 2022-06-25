from aiogram import Dispatcher, Bot, types

from ParserBot5ka.my_parser import selected_stores

token = "5387713157:AAHc0bfR2F8m1WzPiCfPa4_ACi0K39VCZV4"
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = [selected_stores.get(key) for key in selected_stores]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer('Пожалуйста, выберите магазин', reply_markup=keyboard)