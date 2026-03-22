import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8784516259:AAE2030kvj3TUI24myprFXSbJG8lDzDZYqs"
OPENROUTER_API_KEY = "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"

def get_summary(keyword):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4.1-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant who gives brief summaries."},
            {"role": "user", "content": f"Give a short summary about '{keyword}' for a student."}
        ],
        "temperature": 0.5
    }
    try:
        response = requests.post(url, headers=headers, json=data, timeout=15)
        resp_json = response.json()

        # Check if 'choices' exists
        if 'choices' in resp_json and len(resp_json['choices']) > 0:
            return resp_json['choices'][0]['message']['content']
        elif 'error' in resp_json:
            return f"API error: {resp_json['error']}"
        else:
            return f"Summary fetch nahi ho payi 😅 (Unexpected response)"
    except Exception as e:
        return f"Summary fetch nahi ho payi 😅 (Exception: {e})"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text.startswith("@ewfffff_bot"):
        keyword = text.replace("@ewfffff_bot", "").strip()
        if keyword:
            summary = get_summary(keyword)
            await update.message.reply_text(summary)
        else:
            await update.message.reply_text("Bhai, keyword bhi type karna padega!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! Type @ewfffff_bot <keyword> to get a brief summary.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot running...")
    app.run_polling()
