from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from app.services.api_service import fetch_categories

async def categories(update: Update, context: ContextTypes.DEFAULT_TYPE):
    categories = fetch_categories()
    if categories:
        message = "\n".join([f"- {category['name']}" for category in categories])
        response = f"Available categories:\n\n{message}"
    else:
        response = "Sorry, I couldn't fetch the categories. Please try again later."
    
    await update.message.reply_text(response)

categories_handler = CommandHandler("categories", categories)