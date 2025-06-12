from telegram.ext import Updater, MessageHandler, Filters

# ✅ Paste your actual bot token below
TOKEN = '7498679663:AAFAzSC-x9g269LbuO19fkdUHRuwy2WB0J0'

def get_chat_id(update, context):
    chat_id = update.message.chat_id
    print(f"🔑 Chat ID: {chat_id}")
    update.message.reply_text("✅ Got your message! Check the terminal for Chat ID.")

# 🧠 Set up the bot
updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, get_chat_id))

print("🤖 Bot is running. Send a message in the group where the bot is added...")
updater.start_polling()
updater.idle()
