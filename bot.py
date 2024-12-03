import os
from dotenv import load_dotenv
from telegram.ext import Application
from app.handlers.categories import categories_handler

load_dotenv(override=True)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT = os.getenv("PORT", 5000)

def main():
    # Create the Application object with your bot's API token
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add a command handler for /start
    application.add_handler(categories_handler)

    # Set up the webhook
    application.run_webhook(
        listen="0.0.0.0",
        port=int(PORT),  # Render sets the PORT environment variable
        url_path="",
        webhook_url=WEBHOOK_URL,
    )

if __name__ == "__main__":
    main()
