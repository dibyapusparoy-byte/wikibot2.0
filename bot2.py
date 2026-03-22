import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Telegram bot token
TOKEN = "8784516259:AAE2030kvj3TUI24myprFXSbJG8lDzDZYqs"

# OpenRouter API key
OPENROUTER_API_KEY = "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"

# Function to fetch summary from OpenRouter GPT
def get_summary(keyword):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4.1-mini",  # ya gpt-3.5-turbo
        "messages": [
            {"role": "system", "content": "You are a helpful assistant who gives brief summaries."},
            {"role": "user", "content": f"Give a short, clear summary about '{keyword}' for a student."}
        ],
        "temperature": 0.5
    }
    response = requests.post(url, headers=headers, json=data).json()
    try:
        return response['choices'][0]['message']['content']
    except:
        return "Sorry bhai, summary fetch nahi ho payi 😅"

# Function to handle messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text.startswith("@ewfffff_bot"):
        # Extract keyword
        keyword = text.replace("@ewfffff_bot", "").strip()
        if keyword:
            summary = get_summary(keyword)
            await update.message.reply_text(summary)
        else:
            await update.message.reply_text("Bhai, keyword bhi type karna padega!")

# Start bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! Type @ewfffff_bot <keyword> to get a brief summary.")

# Main
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot running...")
app.run_polling()
