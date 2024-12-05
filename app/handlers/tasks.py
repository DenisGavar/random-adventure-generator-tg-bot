from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from app.services.api_service import fetch_tasks

async def tasks(update: Update, context: CallbackContext):
    user = update.effective_user

    data = {}
    if user.id:
        data["telegram_id"] = user.id

    user_input = ' '.join(context.args)
    data["status"] = user_input.strip() if user_input else None

    tasks = fetch_tasks(data)
    if tasks:
        message = "\n".join([
            f"- **Task ID**: {task['task_id']}\n"
            f"  **Description**: {task['description']}\n"
            f"  **Category**: {task['category_name']}\n"
            f"  **Status**: {task['status']}\n"
            f"  **Assigned At**: {task['assigned_at']}\n"
            f"  **Completed At**: {task['completed_at'] or 'Not completed'}\n"
            for task in tasks
        ])
        response = f"Your tasks:\n\n{message}"
    else:
        response = "Sorry, I couldn't fetch the tasks. Please try again later."
    
    await update.message.reply_text(response)

tasks_handler = CommandHandler("tasks", tasks)