# filename: bot.py
import wikipedia
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8784516259:AAE2030kvj3TUI24myprFXSbJG8lDzDZYqs"  # Telegram bot token daal do

# Wikipedia summary function
def get_wikipedia_summary(keyword):
    try:
        wikipedia.set_lang("en")
        return wikipedia.summary(keyword, sentences=3)
    except wikipedia.DisambiguationError as e:
        return f"Multiple results found 😅 Try more specific: {e.options[0]}"
    except wikipedia.PageError:
        return f"Bhai, Wikipedia pe '{keyword}' nahi mila 😅"
    except Exception as e:
        return f"Kuch galat ho gaya 😅 (Error: {e})"

# Handle messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text.startswith("@ewfffff_bot"):
        keyword = text.replace("@ewfffff_bot", "").strip()
        if not keyword:
            await update.message.reply_text("Bhai, keyword type karna zaruri hai!")
            return
        summary = get_wikipedia_summary(keyword)
        await update.message.reply_text(summary)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! Type @ewfffff_bot <keyword> to get a short Wikipedia summary.")

# Main
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot running…")
    app.run_polling()
