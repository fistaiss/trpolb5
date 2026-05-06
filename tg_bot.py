import telebot

TOKEN = "YOUR_TOKEN_HERE"

bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я Telegram-бот 👋")

# Команда /help
@bot.message_handler(commands=['help'])
def help_command(message):
    text = (
        "Доступные команды:\n"
        "/start - запуск бота\n"
        "/help - список команд\n"
    )
    bot.send_message(message.chat.id, text)

# Обработка обычных сообщений
@bot.message_handler(func=lambda message: True)
def echo(message):
    user_text = message.text

    if user_text.lower() == "привет":
        bot.send_message(message.chat.id, "Привет 👋")
    elif user_text.lower() == "пока":
        bot.send_message(message.chat.id, "Пока! 👋")
    else:
        bot.send_message(message.chat.id, "Ты написал: " + user_text)

# Запуск бота
def main():
    print("Бот запущен...")
    bot.polling(none_stop=True)

# Точка входа
if __name__ == "__main__":
    main()
