import os
from dotenv import load_dotenv
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application
from app.handlers.categories import categories_handler

load_dotenv(override=True)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT = os.getenv("PORT")

app = Flask(__name__)

application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
application.add_handler(categories_handler)

@app.route(f"/{TELEGRAM_BOT_TOKEN}", methods=["POST"])
def webhook():
    json_update = request.get_json()
    update = Update.de_json(json_update, application.bot)
    application.update_queue().put(update)
    return "OK", 200

@app.before_first_request
def setup_webhook():
    webhook_url = f"{WEBHOOK_URL}/{TELEGRAM_BOT_TOKEN}"
    application.bot.set_webhook(url=webhook_url)

if __name__ == "__main__":
    app.run(port=PORT)