import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.constants import ChatMemberStatus

# Replace with your actual bot token
TOKEN = "8672169345:AAGAE5R-pbFQteCUkjKM-3DkP5rgp3_fPc4"

# YOUR SPECIFIC TARGETS
TARGET_CHAT_ID = -1002800090700
TARGET_TOPIC_ID = 290

async def get_ids(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends the Chat ID and Topic ID (if applicable)"""
    chat_id = update.effective_chat.id
    topic_id = update.effective_message.message_thread_id
    
    response = f"🆔 **Chat ID:** `{chat_id}`\n"
    response += f"Topic ID: `{topic_id if topic_id else 'None'}`"
    
    await update.message.reply_text(response, parse_mode="Markdown")

async def send_attendance_poll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # STILL CHECK ADMIN STATUS in the chat where command is typed
    member = await context.bot.get_chat_member(update.effective_chat.id, user_id)
    if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        return 

    # Date Logic
    today = datetime.date.today()
    current_day = today.isoweekday()

    if current_day < 5: 
        target_date = today + datetime.timedelta(days=1)
    elif current_day == 5: 
        target_date = today + datetime.timedelta(days=3)
    elif current_day == 6: 
        target_date = today + datetime.timedelta(days=2)
    else: 
        target_date = today + datetime.timedelta(days=1)

    poll_title = target_date.strftime("%A").upper()
    options = ["PRESENT ✅", "ABSENT ❌"]

    # SEND TO THE SPECIFIC CHAT AND TOPIC
    await context.bot.send_poll(
        chat_id=TARGET_CHAT_ID,
        message_thread_id=TARGET_TOPIC_ID, # Forces poll into topic 290
        question=f"ATTENDANCE FOR {poll_title}",
        options=options,
        is_anonymous=False,
        allows_multiple_answers=False
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("poll", send_attendance_poll))
    app.add_handler(CommandHandler("getid", get_ids))

    print(f"Bot running. Polls will be sent to Chat {TARGET_CHAT_ID}, Topic {TARGET_TOPIC_ID} 🚀")
    app.run_polling()
