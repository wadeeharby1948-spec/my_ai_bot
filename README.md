# Hermes Agent - Telegram Bot (Cloud Deployment)

متكامل مع Google Gemini AI ويعمل 24/7 على سيرفر سحابي مجاني.

## المتطلبات

- حساب [GitHub](https://github.com)
- حساب [Replit](https://replit.com) أو [Fly.io](https://fly.io)
- توكن بوت التيليجرام من [@BotFather](https://t.me/BotFather)
- مفتاح Gemini API من [Google AI Studio](https://aistudio.google.com)

## الخطوات

### 1. رفع الكود على GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/username/repo-name.git
git push -u origin main
```

### 2. النشر على Replit (مجاني)

1. ادخل على [replit.com](https://replit.com)
2. اضغط **+ Create Repl**
3. اختر **Import from GitHub**
4. أدخل رابط المستودع
5. اضغط **Import**
6. في Secrets (القيفل الأيسر):
   - `TELEGRAM_BOT_TOKEN` = توكن البوت
   - `TELEGRAM_ALLOWED_USERS` = معرف المستخدم
   - `GEMINI_API_KEY` = مفتاح Gemini
   - `GOOGLE_API_KEY` = مفتاح Gemini
   - `TELEGRAM_WEBHOOK_SECRET` = اضغط Generate
7. اضغط **Run**

### 3. النشر على Fly.io (مجاني)

```bash
# تثبيت Fly CLI
curl -L https://fly.io/install.sh | sh

# تسجيل الدخول
fly auth login

# إنشاء التطبيق
fly launch --no-deploy

# إضافة المتغيرات
fly secrets set TELEGRAM_BOT_TOKEN="your_token"
fly secrets set TELEGRAM_ALLOWED_USERS="your_user_id"
fly secrets set GEMINI_API_KEY="your_key"
fly secrets set GOOGLE_API_KEY="your_key"
fly secrets set TELEGRAM_WEBHOOK_URL="https://your-app.fly.dev/telegram"
fly secrets set TELEGRAM_WEBHOOK_SECRET="$(openssl rand -hex 32)"

# النشر
fly deploy
```

### 4. الحصول على User ID

أرسل رسالة إلى [@userinfobot](https://t.me/userinfobot) لتحصل على معرفك الرقمي.

## الأوامر المتاحة

- `/start` - بدء المحادثة
- `/new` - محادثة جديدة
- `/reset` - إعادة تعيين السياق
- `/model` - تغيير النموذج
- `/status` - حالة البوت
- `/usage` - استخدام السياق

## ملاحظات

- البوت يعمل 24/7 على السيرفر السحابي
- Gemini Flash مجاني من Google AI Studio
- الذاكرة محفوظة بين الجلسات
