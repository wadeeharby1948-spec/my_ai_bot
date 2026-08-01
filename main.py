import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai

# 1. إنشاء سيرفر خفيف لإبقاء البوت حياً
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is online and working!"

def run_flask():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

# 2. إعداد مفاتيح الذكاء الاصطناعي والتيليجرام
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# ذاكرة المحادثات لكل مستخدم
chat_sessions = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك! أنا مساعدك الذكي الشغال 24/7. كيف يمكنني مساعدتك اليوم؟")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_text = update.message.text

    # إنشاء جلسة ذاكرة للمستخدم إذا لم تكن موجودة
    if user_id not in chat_sessions:
        chat_sessions[user_id] = model.start_chat(history=[])

    try:
        chat = chat_sessions[user_id]
        response = chat.send_message(user_text)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text(f"حدث خطأ أثناء المعالجة: {e}")

if __name__ == '__main__':
    # تشغيل السيرفر الخفيف في الخلفية
    threading.Thread(target=run_flask).start()

    # تشغيل بوت التيليجرام
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Bot is starting...")
    application.run_polling()
