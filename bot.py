import logging
import os
from dotenv import load_dotenv
from telegram import Update, InputFile
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Load environment variables from .env file
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Get the bot token securely

WELCOME_IMAGE_PATH = "BMY COIN POST.jpg"  # Ensure the image file is in the same folder

# Enable logging
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Welcome message when user starts the bot
async def start(update: Update, context: CallbackContext):
    user = update.effective_user  # Get user details
    
    # Send image first
    with open(WELCOME_IMAGE_PATH, "rb") as image:
        await update.message.reply_photo(photo=InputFile(image))

    # Welcome text
    welcome_text = (
        f"👋 **Welcome, {user.first_name}!**\n\n"
        "🚀 **BMY Coin** is here to revolutionize the crypto space! Stay ahead with real-time updates, community discussions, and exclusive insights. 🌟\n\n"
        "💎 **Why Join Us?**\n"
        "🔹 Latest updates on BMY Coin\n"
        "🔹 Engage with our thriving community\n"
        "🔹 Exclusive insights and announcements\n\n"
        "📢 **Stay Connected with Us:**"
    )
    
    follow_text = (
        "📌 [Join Telegram](https://t.me/bmycoincrypto) – Community discussions & updates\n"
        "📌 [Follow on Twitter/X](https://x.com/BMYOFFICIALCoin?t=EBf6ujB0yfq425qpU3x77Q&s=09) – Latest tweets & insights\n"
        "📌 [Instagram](https://www.instagram.com/bmy.coin?igsh=cmN0bWhqa2FveXVv) – Exclusive content & behind the scenes"
    )

    await update.message.reply_text(welcome_text, parse_mode="Markdown")
    await update.message.reply_text(follow_text, parse_mode="Markdown")

# Handle all other messages
async def message_handler(update: Update, context: CallbackContext):
    await update.message.reply_text("👋 Welcome to BMY Coin! Type /start to get the latest updates.")

# Error handler to catch exceptions
async def error_handler(update: object, context: CallbackContext):
    logger.error(f"Error: {context.error}")

# Main function to run the bot
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    # Error handler
    app.add_error_handler(error_handler)

    logger.info("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
