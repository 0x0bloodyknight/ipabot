import telebot
import config
from tpparser import get_transcription

API_TOKEN = config.token

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["ipa"])
def handle_ipa(message):
    bot.send_chat_action(message.chat.id, "typing")
    transcription = ""
    if hasattr(message.reply_to_message, "text") and len(message.text) == 4:
        transcription = get_transcription(message.reply_to_message.text)
    else:
        transcription = get_transcription(message.text)
    bot.send_chat_action(message.chat.id, "typing")
    if transcription != "":
        bot.reply_to(message, text=transcription)
    else:
        bot.reply_to(message, "Transcription unavailable")


@bot.message_handler(func=lambda message: message.chat.type == "private")
def handle_private_chat(message):
    bot.send_chat_action(message.chat.id, "typing")
    transcription = get_transcription(message.text)
    bot.send_chat_action(message.chat.id, "typing")
    if transcription != "":
        bot.send_message(message.chat.id, text=transcription)
    else:
        bot.reply_to(message, "Transcription unavailable")


bot.polling()
