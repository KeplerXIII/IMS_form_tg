from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from dotenv import load_dotenv
from mailer import send_email
import os, json

load_dotenv()

bot = Bot(os.getenv('TG_API'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Контакты'))
    keyboard.add(types.KeyboardButton('Отправить заявку', web_app=WebAppInfo(url='https://keplerxiii.github.io/IMS_form_tg/')))
    keyboard.add()
    await message.answer('Добрый день! Рады вас видеть, вы можете получить контакты и оставить заявку', reply_markup=keyboard)

@dp.message_handler(text='Контакты')
async def contacts(message: types.Message):
    keyboard_inline = types.InlineKeyboardMarkup()
    keyboard_inline.add(types.KeyboardButton('Сайт компании', url='https://imsolution.ru/'))
    keyboard_inline.add(types.KeyboardButton('Сайт BrightSign', url='https://imsolution.ru/product'))
    keyboard_inline.add(types.KeyboardButton('Каталог', url='https://imsolution.ru/product'))
    keyboard_inline.add(types.KeyboardButton('Техподдержка', url='https://imsolution.intradesk.ru/dashboard'))
    keyboard_inline.add()
    await message.answer('IMS\nОтдел продаж: +7(495)648-35-05 доб. 107\nРуководитель отдела продаж: +7(495)648-35-05 доб. 120', reply_markup=keyboard_inline)

@dp.message_handler(content_types=['web_app_data'])
async def web_app(mesage: types.Message):
    res = json.loads(mesage.web_app_data.data)
    sender_email = os.getenv('USER')
    sender_password = os.getenv('PASSWORD')
    receiver_email = os.getenv('MAIL_RECIEVER')
    subject = 'Обращение из Телеграмм бота'
    message = f'Имя: {res["name"]}\nПочта: {res["email"]}\nТелефон: {res["phone"]}\nТекст обращения: {res["text"]}'

    result = await send_email(sender_email, sender_password, receiver_email, subject, message)
    await mesage.answer(result)

executor.start_polling(dp)