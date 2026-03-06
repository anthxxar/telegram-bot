import telebot
import random

from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

quotes = [
    "Не здавайся.",
    "Дисципліна сильніша за мотивацію.",
    "PAAAAM paapaprar",
    "Навчання — це інвестиція в себе.",
    "Успіх приходить до тих, хто діє."
]

hi = [
    "Привіт."
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт! Напиши /quote щоб отримати цитату 💬")

@bot.message_handler(commands=['quote'])
def send_quote(message):
    quote = random.choice(quotes)
    bot.send_message(message.chat.id, quote)

@bot.message_handler(commands=['hi'])
def send_hi(message):
    bot.send_message(message.chat.id, random.choice(hi))

bot.polling()
