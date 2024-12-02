import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from app.handlers.categories import categories_handler
#from app.handlers.start import start_handler

load_dotenv(override=True)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(categories_handler)
    #app.add_handler(start_handler)

    app.run_polling()

if __name__ == "__main__":
    main()