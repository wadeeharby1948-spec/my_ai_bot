# Hermes Agent - Telegram Bot

متكامل مع Hugging Face AI ويعمل 24/7 على سيرفر سحابي مجاني.

## المتطلبات

- حساب [GitHub](https://github.com)
- حساب [Replit](https://replit.com)
- توكن بوت التيليجرام من [@BotFather](https://t.me/BotFather)
- توكن Hugging Face من [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

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
   - `HF_TOKEN` = توكن Hugging Face
   - `TELEGRAM_BOT_TOKEN` = توكن البوت
   - `TELEGRAM_ALLOWED_USERS` = معرف المستخدم
7. اضغط **Run**

### 3. الحصول على User ID

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
- Hugging Face مجاني لحد 1000 طلب/شهر مع توكن
- الذاكرة محفوظة بين الجلسات
