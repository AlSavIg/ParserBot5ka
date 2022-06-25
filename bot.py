from aiogram import Dispatcher, Bot, types
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor

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


def send_message(message, shop_id):
    pass


@dp.message_handler(Text(equals=selected_stores.get('5677')))
async def shop5677(message: types.Message):
    await send_message(message=message, shop_id='5677')


@dp.message_handler(Text(equals=selected_stores.get('33YU')))
async def shop33YU(message: types.Message):
    await send_message(message=message, shop_id='33YU')


@dp.message_handler(Text(equals=selected_stores.get('5593')))
async def shop5593(message: types.Message):
    await send_message(message=message, shop_id='5593')


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()