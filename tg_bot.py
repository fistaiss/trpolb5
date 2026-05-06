import telebot
import logging
from datetime import datetime

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Вставь сюда свой токен
TOKEN = 'ТВОЙ_ТОКЕН_ЗДЕСЬ'
bot = telebot.TeleBot(TOKEN)

# 1. Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    welcome_text = (
        f"Привет, {user_name}! 👋\n"
        "Я учебный бот, созданный для лабораторной работы №5.\n"
        "Используй /help, чтобы увидеть список моих возможностей."
    )
    bot.reply_to(message, welcome_text)
    logging.info(f"Пользователь {user_name} запустил бота")

# 2. Обработка команды /help
@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "🤖 **Доступные команды:**\n\n"
        "/start - Запустить бота\n"
        "/help - Показать это меню\n"
        "/time - Узнать текущее время\n"
        "/status - Проверить состояние проекта"
    )
    bot.send_message(message.chat.id, help_text, parse_mode='Markdown')

# 3. Дополнительная функция: Текущее время
@bot.message_handler(commands=['time'])
def show_time(message):
    now = datetime.now().strftime("%H:%M:%S")
    bot.reply_to(message, f"Текущее время: {now} ⏰")

# 4. Дополнительная функция: Статус
@bot.message_handler(commands=['status'])
def check_status(message):
    status_report = (
        "📊 **Статус разработки:**\n"
        "- Базовая логика: Готова\n"
        "- Интеграция AI: Выполнена\n"
        "- Git-репозиторий: Настроен\n"
        "Версия: 1.0.2"
    )
    bot.send_message(message.chat.id, status_report, parse_mode='Markdown')

# 5. Эхо-ответ
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Ты написал: '{message.text}'. Я пока только учусь!")

# Запуск бота
if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()