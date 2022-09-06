import telebot
import random

token = "5696827150:AAEoHowy4AxQhZZecYa5dkiSO70sxA-noGk"

bot = telebot.TeleBot(token)

RANDOM_TASKS = ["Записаться на курс в Нетологию", "Написать Гвидо письмо", "Покормить кошку", "Помыть машину"]

HELP = """
/help - напечатать справку по программе.
/add - добавить задачу в список (название задачи запрашиваем у пользователя).
/show - напечатать все добавленные задачи.
/random - добавлять случайную задачу на дату Сегодня"""

tasks = {
    }

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = [task]  # Создание ключа и определения к нему сразу же


@bot.message_handler(command=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    if len(task) < 3:
        bot.send_message(message.chat.id, "Неверный формат задачи")
    else:
        add_todo(date, task)
        text = "Задача " + task + " добавлена на дату " + date
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(message):
    date = "сегондя"
    task = random.choise(RANDOM_TASKS)
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split()[0] # show сегодня 31.12 завтра
    dates = [dt.lower() for dt in message.text.split()[1:]]
    text = ""
    for date in dates:
        if date in tasks:
            text = date.lower() + "\n"
            for task in tasks[date]:
                text = text + "[] " + task + "\n"
        else:
            text = "Задач на эту дату нет"
        bot.send_message(message.chat.id, text)


# Постоянно обращается к серверам телеграм
bot.polling(non_stop=True)