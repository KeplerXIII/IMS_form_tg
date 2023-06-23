from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from dotenv import load_dotenv
import os, json

load_dotenv()

bot = Bot(os.getenv('TG_API'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Каталог', url='https://imsolution.ru/product'))
    keyboard.add(types.KeyboardButton('Отправить заявку', web_app=WebAppInfo(url='https://keplerxiii.github.io/IMS_form_tg/'), request_contact=True))
    
    keyboard.add()
    await message.answer('Добрый день! Рады вас видеть, можете ознакомиться с каталогом товаров и оставить заявку', reply_markup=keyboard)

@dp.message_handler(content_types=['web_app_data'])
async def web_app(mesage: types.Message):
    res = json.loads(mesage.web_app_data.data)
    print(res)
    await mesage.answer(res)

executor.start_polling(dp)