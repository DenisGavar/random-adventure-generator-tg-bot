from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from app.services.api_service import generate_new_task

async def generate_task(update: Update, context: CallbackContext):
    user = update.effective_user

    task_data = {}

    if user.id:
        task_data["telegram_id"] = user.id

    user_input = ' '.join(context.args)
    task_data["category"] = user_input.strip() if user_input else None
    
    task, error_message = generate_new_task(task_data)

    if task:
        response = f"Your task in category '{task['category']}' is:\n\n{task['description']}"
    elif error_message:
        response = error_message
    else:
        response = "Something went wrong"
    
    await update.message.reply_text(response)


generate_task_handler = CommandHandler("generate_task", generate_task)