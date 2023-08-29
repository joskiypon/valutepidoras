python
import requests
from telegram.ext import Updater, CommandHandler

def exchange_rates(update, context):
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    data = response.json()
    rates = data["rates"]
    message = "Текущие обменные курсы:\n"
    for currency, rate in rates.items():
        message += f"{currency}: {rate}\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    updater = Updater(token="6664161204:AAGSswUPuGzZsjjvfDV2ktWLuDXrc9i_O-o", use_context=True)
    dispatcher = updater.dispatcher
    exchange_handler = CommandHandler('в', exchange_rates)
    dispatcher.add_handler(exchange_handler)
    updater.start_polling()

if name == 'main':
    main()