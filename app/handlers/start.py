from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from app.services.api_service import register_user

async def start(update: Update, context: CallbackContext):
    user = update.effective_user

    user_data = {}

    if user.id:
        user_data["telegram_id"] = user.id
    if user.first_name:
        user_data["first_name"] = user.first_name
    if user.username:
        user_data["username"] = user.username
    if user.last_name:
        user_data["last_name"] = user.last_name
    
    user = register_user(user_data)

    if user:
        response = "You have been successfully registered!"
    else:
        response = "Registration failed. Please try again later."
    
    await update.message.reply_text(response)


start_handler = CommandHandler("start", start)