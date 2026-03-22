# filename: bot.py
from googlesearch import search
import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "YOUR_BOT_TOKEN_HERE"

# Get top Google search result safely
def get_google_summary(keyword):
    try:
        # Try top 1 result
        results = list(search(keyword, num_results=1))
        if not results:
            return "Bhai, search result nahi mila 😅"
        url = results[0]

        # Fetch page content safely
        try:
            resp = requests.get(url, timeout=10)
            soup = BeautifulSoup(resp.text, "html.parser")
            paragraphs = soup.find_all('p')
            for p in paragraphs:
                text = p.get_text().strip()
                if len(text) > 50:
                    return text  # return first meaningful paragraph
            return f"Top result: {url}"  # fallback
        except:
            return f"Top result URL: {url}"

    except Exception:
        return "Bhai, search failed 😅 Try a different keyword!"

# Handle messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text.startswith("@ewfffff_bot"):
        keyword = text.replace("@ewfffff_bot", "").strip()
        if not keyword:
            await update.message.reply_text("Bhai, keyword type karna zaruri hai!")
            return
        summary = get_google_summary(keyword)
        await update.message.reply_text(summary)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! Type @ewfffff_bot <keyword> to get a short summary from Google search.")

# Main
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot running…")
    app.run_polling()
