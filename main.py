import telebot
import config
from tpparser import get_transcription
from telebot import types

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
    if transcription != "":
        bot.reply_to(message, text=transcription)
    else:
        bot.reply_to(message, "Transcription unavailable")


@bot.message_handler(func=lambda message: message.chat.type == "private")
def handle_private_chat(message):
    bot.send_chat_action(message.chat.id, "typing")
    transcription = ""
    transcription = get_transcription(message.text)
    if transcription != "":
        bot.send_message(message.chat.id, text=transcription)
    else:
        bot.reply_to(message, "Transcription unavailable")


@bot.inline_handler(lambda query: query.query.isascii() == True)
def query_text(inline_query):
    transcription = ""
    transcription = get_transcription(inline_query.query)
    if transcription != "":
        res = types.InlineQueryResultArticle(
            "1", transcription, types.InputTextMessageContent(transcription)
        )
        bot.answer_inline_query(inline_query.id, [res])
    else:
        res = types.InlineQueryResultArticle(
            "1",
            inline_query.query,
            types.InputTextMessageContent(inline_query.query),
        )
    bot.answer_inline_query(inline_query.id, [res])


bot.polling()
