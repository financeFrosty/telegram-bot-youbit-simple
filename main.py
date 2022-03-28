import requests
from datetime import datetime
import telebot
import os

token = os.environ['token']


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, 
            "Привет! Введи команду price что бы узнать курс BTC to USD на бирже yobit.net")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "price":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                sell_price = response["btc_usd"]["sell"]  
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}"
                )
            except Exception as ex:
                bot.send_message(
                    message.chat.id,
                    f"Что то пошло не так"
                )
        else:
            bot.send_message(message.chat.id, "Неправильная команда")

    bot.polling()

def main():
    telegram_bot(token)

if __name__ == "__main__":
    main()