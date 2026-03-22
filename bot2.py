# filename: bot_gemini.py
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ====== CONFIG ======
TOKEN = "8784516259:AAE2030kvj3TUI24myprFXSbJG8lDzDZYqs"   # Telegram bot token daal do
GEMINI_API_KEY = "AIzaSyC2QX1EVPCcEZnG_77vh8rqOkkDKgIfkJE"  # Gemini API key

# ====== Gemini API function ======
def get_gemini_summary(keyword):
    try:
        url = "https://api.gemini.com/v1/complete"  # Example endpoint, replace with actual if needed
        headers = {
            "Authorization": f"Bearer {GEMINI_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "gemini-1.5",  # ya jo bhi available model hai
            "prompt": f"Give a short, clear summary about '{keyword}' for a student.",
            "temperature": 0.5,
            "max_output_tokens": 200
        }
        resp = requests.post(url, json=data, headers=headers, timeout=10).json()
        # Try to extract the response text
        try:
            return resp["output"][0]["content"][0]["text"]
        except:
            return "Bhai, summary fetch nahi ho payi 😅"
    except Exception as e:
        return f"Kuch galat ho gaya 😅 (Error: {e})"

# ====== Telegram handlers ======
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text.startswith("@ewfffff_bot"):
        keyword = text.replace("@ewfffff_bot", "").strip()
        if not keyword:
            await update.message.reply_text("Bhai, keyword type karna zaruri hai!")
            return
        summary = get_gemini_summary(keyword)
        await update.message.reply_text(summary)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! Type @ewfffff_bot <keyword> to get a short summary from Gemini AI.")

# ====== Main ======
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot running…")
    app.run_polling()
