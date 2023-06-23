import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()


async def send_email(sender_email, sender_password, receiver_email, subject, message):
    # Создание объекта MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Добавление сообщения в формате HTML или простого текста
    body = MIMEText(message, 'plain')
    msg.attach(body)

    try:
        # Создание SMTP-соединения с сервером Yandex
        smtp_server = 'smtp.yandex.ru'
        smtp_port = 587
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()

        # Авторизация на сервере
        smtp_connection.login(sender_email, sender_password)

        # Отправка письма
        smtp_connection.sendmail(sender_email, receiver_email, msg.as_string())
        answer = ('Письмо успешно отправлено!')

        # Закрытие соединения
        smtp_connection.quit()
    except Exception as e:
        answer = 'Возникла ошибка при отправке заявки:' + str(e)

    return answer

# # Пример использования функции send_email
# sender_email = os.getenv('USER')
# sender_password = os.getenv('PASSWORD')
# receiver_email = os.getenv('MAIL_RECIEVER')
# subject = 'Тестовое письмо'
# message = 'Привет, это тестовое письмо!'

# print(asyncio.run(send_email(sender_email, sender_password, receiver_email, subject, message)))