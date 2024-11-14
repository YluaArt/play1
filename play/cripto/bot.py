import telebot
token = '7561878862:AAHTxQeZjWiad2L5ozLwjfwSPI2TRma_Tjs'

bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_message(message_text):
    bot.send_message(5235680239, message_text)

