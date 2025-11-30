import telebot
import config
import api
import schedule

bot = telebot.TeleBot(config.tg_bot_api)

chat_id = None
information = [api.name_surname, api.scores, api.print_events()]


@bot.message_handler(commands=['start'])
def welcome(message):
    global chat_id
    chat_id = message.chat.id

    bot.send_message(chat_id, "Hi, man.")

    schedule.every(10).seconds.run(send_information(information))

def send_information(messages):
    for i in messages:
        bot.send_message(chat_id, i)


bot.infinity_polling()
