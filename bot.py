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



import os
from dotenv import load_dotenv
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from app.handlers.categories import categories_handler

load_dotenv(override=True)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT = os.getenv("PORT", 5000)

# Initialize Flask app
app = Flask(__name__)

# Initialize the Telegram bot application
bot_app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

# Add the /start handler
bot_app.add_handler(categories_handler)

@app.route("/", methods=["POST"])
def webhook():
    """Endpoint to receive webhook updates from Telegram."""
    json_data = request.get_json()
    update = Update.de_json(json_data, bot_app.bot)
    bot_app.update_queue.put(update)
    return "OK", 200

@app.route("/set_webhook", methods=["GET"])
def set_webhook():
    """Endpoint to manually set the webhook."""
    bot_app.bot.set_webhook(url=WEBHOOK_URL)
    return f"Webhook set to {WEBHOOK_URL}", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(PORT))
