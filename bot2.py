import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8784516259:AAE2030kvj3TUI24myprFXSbJG8lDzDZYqs"
OPENROUTER_API_KEY = "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"

# 🤖 AI FUNCTION
async def ai_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    user_text = update.message.text.lower()

    # 🔥 FILTER ADD YAHI KARNA HAI
    study_keywords = [
        "what is", "define", "explain", "formula",
        "derive", "numerical", "velocity", "force",
        "mole", "atom", "integration", "derivative"
    ]

    if not any(word in user_text for word in study_keywords):
        return  # ❌ ignore normal chat

    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mistralai/mistral-7b-instruct",
                "messages": [
                    {"role": "user", "content": f"Explain this in simple Class 11/12 level with example:\n{user_text}"}
                ]
            }
        )

        data = response.json()
        reply = data["choices"][0]["message"]["content"]

        await update.message.reply_text(f"🧠 AI Teacher:\n{reply[:1000]}")

    except Exception as e:
        await update.message.reply_text("⚠️ Error getting AI response")
        print(e)

# 🚀 BOT START
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), ai_reply))

print("🚀 OpenRouter AI Bot Running...")

app.run_polling(close_loop=False)
