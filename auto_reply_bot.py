from telegram.ext import Updater, MessageHandler, Filters
import logging

# --- Bot Token ---
TOKEN = '7498679663:AAFAzSC-x9g269LbuO19fkdUHRuwy2WB0J0'

# --- Enable Logging (Optional) ---
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- Define Auto Replies ---
def handle_message(update, context):
    message = update.message.text.strip()
    chat_id = update.message.chat_id
    print(f"📩 Message from {chat_id}: {message}")

    # Match triggers
    if message == "/start":
        context.bot.send_message(chat_id=chat_id, text="✅ This channel is ready to receive videos Respond with y & n (where y=yes n)")

    elif message == "/stop":
        context.bot.send_message(chat_id=chat_id, text="⛔ This channel has stopped receiving videos")

    elif message == "@frank_rono@Joshua_Delamoa@christophermuasya@SyrusOmondi@Elphans_muthii@Josephmwanzia signing in":
        context.bot.send_message(chat_id=chat_id, text="✅ Signing in confirmed")

    elif message == "@frank_rono@Joshua_Delamoa@christophermuasya@SyrusOmondi@Elphans_muthii@Josephmwanzia signing out":
        context.bot.send_message(chat_id=chat_id, text="✅ Signing out confirmed")

    else:
        print("📭 No matching trigger.")

# --- Start Bot ---
updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, handle_message))

print("🤖 Bot is now running with multiple triggers...")
updater.start_polling()
updater.idle()
