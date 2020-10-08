import telebot
import config
from tpparser import get_transcription

API_TOKEN = config.token

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["ipa"])
def handle_ipa(message):
    bot.send_chat_action(message.chat.id, "typing")
    transcription = get_transcription(message.text)
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, text=transcription)


@bot.message_handler(func=lambda message: message.chat.type == "private")
def handle_private_chat(message):
    bot.send_chat_action(message.chat.id, "typing")
    transcription = get_transcription(message.text)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, text=transcription)


bot.polling()