import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.constants import ParseMode, ChatMemberStatus

# Replace with your actual bot token
TOKEN = "8784516259:AAE2030kvj3TUI24myprFXSbJG8lDzDZYqs"

async def send_attendance_poll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    # Check if the user is an admin or creator
    member = await context.bot.get_chat_member(chat_id, user_id)
    if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        return # Ignore non-admins

    # Logic to get the next weekday (Skipping Sat/Sun)
    today = datetime.date.today()
    # isoweekday: 1=Mon, 2=Tue, 3=Wed, 4=Thu, 5=Fri, 6=Sat, 7=Sun
    current_day = today.isoweekday()

    if current_day < 5:  # Mon-Thu: Poll for tomorrow
        target_date = today + datetime.timedelta(days=1)
    elif current_day == 5: # Friday: Poll for Monday
        target_date = today + datetime.timedelta(days=3)
    elif current_day == 6: # Saturday: Poll for Monday
        target_date = today + datetime.timedelta(days=2)
    else: # Sunday: Poll for Monday
        target_date = today + datetime.timedelta(days=1)

    # Format the day name in CAPS
    poll_title = target_date.strftime("%A").upper()
    options = ["PRESENT ✅", "ABSENT ❌"]

    # Send the real Telegram poll
    await context.bot.send_poll(
        chat_id=chat_id,
        question=f"ATTENDANCE FOR {poll_title}",
        options=options,
        is_anonymous=False, # Non-anonymous so you can see who voted
        allows_multiple_answers=False
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Add the /poll command handler
    app.add_handler(CommandHandler("poll", send_attendance_poll))

    print("Bot is running. Only Admins can use /poll 🚀")
    app.run_polling()
