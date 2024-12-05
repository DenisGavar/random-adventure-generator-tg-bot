import os
import logging
import json
from dotenv import load_dotenv
from quart import Quart, request, jsonify
from telegram import Update
from telegram.ext import Application
from app.handlers.categories import categories_handler
from app.handlers.start import start_handler
from app.handlers.generate import generate_task_handler
from app.handlers.get import get_task_handler
from app.handlers.tasks import tasks_handler
from app.handlers.complete import complete_task_handler

load_dotenv(override=True)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT = os.getenv("PORT")

# Initialize Quart app
app = Quart(__name__)

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Application instance
application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

# Add handlers to the application
application.add_handler(categories_handler)
application.add_handler(start_handler)
application.add_handler(generate_task_handler)
application.add_handler(get_task_handler)
application.add_handler(tasks_handler)
application.add_handler(complete_task_handler)

# Initialize the Application properly
@app.before_serving
async def before_serving():
    # Await the initialization of the Application
    await application.initialize()

@app.route("/set_webhook", methods=["GET"])
async def set_webhook():
    """Set the webhook for the bot."""
    response = await application.bot.set_webhook(WEBHOOK_URL)
    if response:
        return f"Webhook set to {WEBHOOK_URL}", 200
    else:
        return "Failed to set webhook", 500

@app.route("/", methods=["POST"])
async def webhook():
    """Handle incoming updates from Telegram."""
    logger.info("Webhook received")
    
    # Get the raw data from the POST request and decode it as a string
    json_str = await request.get_data()
    
    # Parse the string into a JSON object (dictionary)
    update_data = json.loads(json_str.decode('utf-8'))
    
    # Use the parsed data to create an Update object
    update = Update.de_json(update_data, application.bot)
    
    # Process the update
    await application.process_update(update)
    
    return jsonify({'status': 'ok'}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
