# Задача 2. Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000. 
# Когда игрок угадывает его, бот выводит количество сделанных ходов.

from email.mime import message
import telebot
import math
import requests
import os

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    global number
    number = int(input("Введите число от 1 до 1000: "))
    global count_move
    count_move = 0
    bot.send_message(message.from_user.id, "Я загадал число от 1 до 1000, попробуй его отгадать")

@bot.message_handler(content_types=["text"])
def guess_num(message):
    global number
    global count_move
    text = int(message.text)
    count_move += 1
    if text == number:
        bot.send_message(message.from_user.id, f'Поздравляю, Вы отгадали! Количество ходов, которое Вам потребовалось: {count_move}')
    elif abs(number - text) > 500:
        bot.send_message(message.from_user.id,'Очень холодо, загаданное число гораздо больше' if (number - text) > 0 else 'Очень холодо, загаданное число гораздо меньше')
    elif abs(number - text) > 100:
        bot.send_message(message.from_user.id,'Xолодо, загаданное число больше' if (number - text) > 0 else 'Холодо, загаданное число  меньше')
    elif abs(number - text) > 50:
        bot.send_message(message.from_user.id,'Теплее, загаданное несколько больше' if (number - text) > 0 else 'Теплее, загаданное число несколько меньше')
    elif abs(number - text) > 1:
        bot.send_message(message.from_user.id,'Горячо, загаданное число чуть больше' if (number - text) > 0 else '{Горячо, загаданное число чуть меньше')
bot.polling(none_stop = True, interval = 0)