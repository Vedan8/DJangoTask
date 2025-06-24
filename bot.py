import os
import django
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from asgiref.sync import sync_to_async 
from decouple import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoTask.settings")
django.setup()

from api.models import TelegramUser

TOKEN = config("TELEGRAM_TOKEN")  

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    username = update.effective_user.username
    if username:
        
        await sync_to_async(TelegramUser.objects.get_or_create)(username=username)

        await update.message.reply_text(f"Hello, {username}! You have been registered.")
    else:
        await update.message.reply_text("I couldn't get your username. Please set a username in your Telegram settings.")

def run_bot():
    """Run the bot polling."""
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()


if __name__ == '__main__':
    run_bot()
