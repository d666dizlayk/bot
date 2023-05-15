import telebot

bot = telebot.TeleBot('5485149483:AAHq3JCencmxOGzPX3QLa41y0UZ36Zyrm98')
to_chat_id = -1001952434456


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Салам алейкум, сообщите о поломке через меня и скоро её исправят!")
@bot.message_handler(content_types=['text'])
def all_messages(message):
    bot.forward_message(to_chat_id, message.chat.id, message.message_id)
bot.infinity_polling()