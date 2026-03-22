# filename: class11_12_bot_dict_only.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ====== CONFIG ======
TOKEN = "8784516259:AAE2030kvj3TUI24myprFXSbJG8lDzDZYqs"  # Telegram bot token

# ====== Predefined Class 11-12 Topics with 4-5 line definitions + examples ======
topics_dict = {
    "motion": "Motion describes the change in position of an object over time. It can be uniform or non-uniform.\nExamples:\n- A car moving on a straight road\n- A person walking to school\n- Falling of a ball due to gravity",
    "laws of motion": "Newton's laws of motion explain how forces affect the motion of objects.\nExamples:\n- Rocket launch (3rd law)\n- Ball at rest starts moving when pushed (1st law)\n- Car brakes suddenly (2nd law)",
    "rotation": "Rotation is circular movement of an object around a fixed axis.\nExamples:\n- Earth rotating around its axis\n- Wheel spinning on a bicycle",
    "work": "Work is done when a force moves an object through a distance.\nExamples:\n- Lifting a book\n- Pushing a cart\n- Pulling a rope",
    "energy": "Energy is the capacity to do work and exists in forms like kinetic and potential.\nExamples:\n- A stretched rubber band has potential energy\n- A moving car has kinetic energy",
    # … Add all other topics similarly
}

# ====== Telegram Handlers ======
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text.startswith("@ewfffff_bot"):
        keyword = text.replace("@ewfffff_bot", "").strip().lower()
        if not keyword:
            await update.message.reply_text("Bhai, keyword type karna zaruri hai!")
            return
        summary = topics_dict.get(keyword, "Bhai, summary nahi mili 😅")
        await update.message.reply_text(summary)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hey! Type @ewfffff_bot <topic> to get exam-friendly Class 11-12 summary with examples."
    )

# ====== Main ======
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot running…")
    app.run_polling()
