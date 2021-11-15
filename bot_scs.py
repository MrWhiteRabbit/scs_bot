#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
from time import sleep
from threading import Thread
import schedule
from auth_data import auth_data
from auth_data import zoom as z
from auth_data import chat_id as chat_id


bot = telebot.TeleBot(auth_data)


def schedule_checker():

    schedule.run_pending()
    sleep(1)


def poll():

    bot.polling(none_stop=True, interval=0)


def say_good_morning(my_id):

    message = f'Доброе утро!\nЧерез 5 минут встречаемся на daily scrum в Zoom по ссылке:\n{z}'

    return bot.send_message(my_id, message)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '/help':
        bot.send_message(message.from_user.id, f'/link - ссылка на Zoom SM')

    elif message.text == '/link':
        bot.send_message(message.from_user.id, f'Для подключения к конференции используйте ссылку: \n{z}')


if __name__ == '__main__':

    schedule.every().day.at("09:55").do(say_good_morning, chat_id)

    Thread(target=poll).start()

    while True:
        schedule_checker()

