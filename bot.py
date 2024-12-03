import os
from dotenv import load_dotenv
from flask import Flask, request
from telegram import Update
from telegram.ext import Application
from app.handlers.categories import categories_handler

load_dotenv(override=True)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT = os.getenv("PORT")

app = Flask(__name__)

application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
application.add_handler(categories_handler)

@app.route('/setwebhook', methods=['GET'])
def set_webhook():
    webhook_url = f"{WEBHOOK_URL}/{TELEGRAM_BOT_TOKEN}"
    s = application.bot.set_webhook(url=webhook_url)
    if s:
        return "Webhook setup successful!"
    else:
        return "Webhook setup failed.", 500

@app.route(f"/{TELEGRAM_BOT_TOKEN}", methods=["POST"])
def webhook():
    json_update = request.get_json()
    try:
        update = Update.de_json(json_update, application.bot)
        application.update_queue.put_nowait(update)
        return "OK", 200
    except Exception as e:
        print(f"Error handling update: {e}")
        return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(port=PORT)