# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.
# Задача 2. Добавьте боту модуль, который позволяет считывать из файла вопрос, 
# отвечать на него и отправлять ответ обратно пользователю.

from email.mime import message
import telebot
import math
import requests
import os

bot = telebot.TeleBot('')

@bot.message_handler(content_types=["text"])
def support(message):
    data = 'id: ' + str(message.from_user.id) + ' '+ str(message.text) + '\n'
    with open("log_support.txt", "a", encoding='utf-8') as file:
        file.writelines(data)
    bot.send_message(message.from_user.id, "Благодарим за обращение! Скоро с Вами свяжется специалист!")
    with open("log_support.txt", "r", encoding='utf-8') as file:
        appeal = file.read()
        appeal = appeal.split("\n")
    new_list = appeal[-2].split(' ')
    problem = ''
    for i in range(2, len(new_list)):
        problem += new_list[i]+' '
    answer = input(f'Необходимо решить проблему пользователя: {problem} ')
    bot.send_message(message.from_user.id, f'Чтобы решить Вашу проблему, необходимо сделать следующее: {answer}')


bot.polling(none_stop = True, interval = 0)