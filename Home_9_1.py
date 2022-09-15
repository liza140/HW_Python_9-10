# Задача 1. Добавьте telegram-боту возможность вычислять выражения: 1 + 4 * 2 -> 9.

from email.mime import message
import telebot
import requests
import os

bot = telebot.TeleBot('')
@bot.message_handler(content_types=["text"])
def math_function(message):
    text = message.text
    dictionary = "абвгдеёжзиклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz"
    flag = True
    for i in range(len(dictionary)):
        if dictionary[i] in text:
            print('Введенное сообщение не является математическим выражением')
            flag = False
            break
    if flag == True:
            print(f'выражение {text} равно {eval(text)}')

bot.polling(none_stop = True, interval = 0)