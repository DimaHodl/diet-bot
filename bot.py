
import logging
from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Временно без GPT — просто тестовая заглушка
def generate_diet_response(message: str) -> str:
    return (
        "Вот пример рациона на день:\n"
        "\nЗавтрак: овсянка на воде с бананом\n"
        "Обед: куриное филе, гречка, салат из огурцов\n"
        "Ужин: тушёные овощи и киноа\n"
        "\n(Это заглушка. GPT подключим, как только появится API Key.)"
    )

# Обработка текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    response = generate_diet_response(user_message)
    await update.message.reply_text(response)

# Старт-бота
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Я ИИ-диетолог. Напиши мне: \n"
        "- свою цель (похудение, набор массы и т.п.)\n"
        "- ограничения (аллергии, гастрит, диабет)\n"
        "- и я составлю тебе рацион!"
    )

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    bot_token = "7884145399:AAEzELcnBppv_FwPrDnCl9cLYizgBrLTlOQ"
    
    app = ApplicationBuilder().token(bot_token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()
