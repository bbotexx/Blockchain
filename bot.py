import config
import telebot
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

bot = telebot.TeleBot(config.token)
rpc_connection = AuthServiceProxy("http://user:password@localhost:8332/")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который повторяет написанное сообщение. "
                          "Для получения нового адреса введи /getnewaddress, для получения баланса - /getbalance.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

@bot.message_handler(commands=['getnewaddress'])
def get_new_address(message):
    new_address = rpc_connection.getnewaddress()
    bot.reply_to(message, f"Новый адрес: {new_address}")

@bot.message_handler(commands=['getbalance'])
def get_balance(message):
    balance = rpc_connection.getbalance()
    bot.reply_to(message, f"Баланс кошелька: {balance}")

if __name__ == "__main__":
    bot.infinity_polling()
