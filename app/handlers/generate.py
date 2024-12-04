from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from app.services.api_service import generate_task

async def generate(update: Update, context: CallbackContext):
    user = update.effective_user

    task_data = {}

    if user.id:
        task_data["telegram_id"] = user.id

    user_input = ' '.join(context.args)
    task_data["category"] = user_input.strip() if user_input else None
    
    task = generate_task(task_data)

    if task:
        response = f"Your task in category '{task['category']}' is:\n\n{task['description']}"
    else:
        response = "Something went wrong"
    
    await update.message.reply_text(response)


generate_handler = CommandHandler("generate", generate)