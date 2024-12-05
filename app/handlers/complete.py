from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from app.services.api_service import complete_user_task

async def complete_task(update: Update, context: CallbackContext):
    user = update.effective_user

    data = {}
    if user.id:
        data["telegram_id"] = user.id

    user_input = ' '.join(context.args)
    data["task_id"] = user_input.strip() if user_input else None
    
    task = complete_user_task(data)

    if task:
        response = "Your task completed successfully"
    else:
        response = "Something went wrong"
    
    await update.message.reply_text(response)


complete_task_handler = CommandHandler("complete_task", complete_task)