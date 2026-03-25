import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.constants import ChatMemberStatus

# Replace with your actual bot token
TOKEN = "8784516259:AAE2030kvj3TUI24myprFXSbJG8lDzDZYqs"

async def get_ids(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends the Chat ID and Topic ID (if applicable)"""
    chat_id = update.effective_chat.id
    # message_thread_id will be None if the group doesn't have topics enabled
    topic_id = update.effective_message.message_thread_id
    
    response = f"🆔 **Chat ID:** `{chat_id}`\n"
    if topic_id:
        response += f"话题 **Topic ID:** `{topic_id}`"
    else:
        response += "话题 **Topic ID:** None (General or not a topic)"
    
    await update.message.reply_text(response, parse_mode="Markdown")

async def send_attendance_poll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    # Capture the thread ID to ensure the poll stays in the same topic
    thread_id = update.effective_message.message_thread_id

    member = await context.bot.get_chat_member(chat_id, user_id)
    if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        return 

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

    await context.bot.send_poll(
        chat_id=chat_id,
        message_thread_id=thread_id, # This sends it to the specific topic
        question=f"ATTENDANCE FOR {poll_title}",
        options=options,
        is_anonymous=False,
        allows_multiple_answers=False
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Register handlers
    app.add_handler(CommandHandler("poll", send_attendance_poll))
    app.add_handler(CommandHandler("getid", get_ids))

    print("Bot is running. Use /poll or /getid 🚀")
    app.run_polling()
