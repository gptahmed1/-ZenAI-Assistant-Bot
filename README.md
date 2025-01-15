# 🤖 ZenAI Assistant Bot

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg">
  <img src="https://img.shields.io/badge/Telegram-Bot-blue.svg">
  <img src="https://img.shields.io/badge/Google-AI-red.svg">
  <img src="https://img.shields.io/badge/License-MIT-green.svg">
</div>

## 📝 الوصف
ZenAI هو مساعد ذكي يعمل على منصة Telegram، مدعوم بتقنية Google AI (Gemini). يقدم البوت مساعدة فورية وذكية للمستخدمين، مع قدرات متقدمة في فهم وتحليل الأسئلة والاستفسارات.

## ✨ المميزات الرئيسية
- 🚀 معالجة سريعة وذكية للاستفسارات
- 🔒 تشفير وحماية متقدمة للبيانات
- 💾 نظام تخزين مؤقت ذكي
- ⚡ أداء عالي مع معالجة متزامنة
- 📊 إدارة معدل الاستخدام
- 🛡️ حماية ضد الهجمات
- 📝 تنسيق ذكي للردود
- 📋 تسجيل متقدم للأحداث

## 🛠️ المتطلبات التقنية
- Python 3.9+
- Telegram Bot Token
- Google AI (Gemini) API Key

## 📦 المكتبات المطلوبة
```
python-telegram-bot==20.7
google-generativeai==0.3.0
python-dotenv==1.0.0
cryptography==41.0.7
cachetools==5.3.2
ratelimit==2.2.1
```

## ⚙️ التثبيت والإعداد

1. استنساخ المشروع:
```bash
git clone https://github.com/yourusername/zenai-bot.git
cd zenai-bot
```

2. إنشاء البيئة الافتراضية:
```bash
python -m venv venv

# Linux/Mac:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

3. تثبيت المتطلبات:
```bash
pip install -r requirements.txt
```

4. إعداد ملف البيئة (.env):
```env
TELEGRAM_TOKEN=your_telegram_token
GEMINI_API_KEY=your_gemini_api_key
```
https://t.me/BotFather
https://aistudio.google.com/app/apikey
رابط استضافة : https://replit.com/
5. تشغيل البوت:
```bash
python main.py
```

## 🚀 كيفية الاستخدام

1. ابدأ محادثة مع البوت على Telegram
2. استخدم الأوامر الأساسية:
   - `/start` - بدء محادثة جديدة
   - `/help` - عرض المساعدة
   - `/reset` - إعادة تعيين المحادثة

3. اكتب سؤالك أو استفسارك بشكل مباشر

## 📈 هيكل المشروع
```
project/
├── config/
│   ├── __init__.py
│   └── settings.py
├── utils/
│   ├── __init__.py
│   ├── security.py
│   ├── cache.py
│   └── helpers.py
├── core/
│   ├── __init__.py
│   ├── bot.py
│   └── handlers.py
├── .env
├── requirements.txt
└── main.py
```

## 🔒 الأمان
- تشفير جميع البيانات المتبادلة
- حماية ضد هجمات DDoS
- إدارة معدل الاستخدام
- تخزين آمن للمفاتيح

## ⚡ الأداء
- معالجة متزامنة للرسائل
- تخزين مؤقت ذكي
- إدارة فعالة للموارد
- استجابة سريعة

## 🤝 المساهمة
نرحب بمساهماتكم! يرجى اتباع الخطوات التالية:
1. Fork المشروع
2. إنشاء فرع للميزة الجديدة
3. تقديم Pull Request

## 📝 الترخيص
هذا المشروع مرخص تحت [MIT License](LICENSE).

## 👥 المطورون
- [[احمد]](https://t.me/QA_1_S) - المطور الرئيسي

## 📞 الدعم
- فتح Issue على GitHub
- التواصل عبر Telegram: [[@YourBotUsername](https://t.me/QA_1_S)]

## 🌟 شكر خاص
- شكر خاص لـ Google AI لتوفير واجهة برمجة التطبيقات
- شكر للمجتمع المفتوح المصدر

## 📚 الوثائق الإضافية
- [دليل المستخدم](docs/USER_GUIDE.md)
- [دليل المطور](docs/DEVELOPER_GUIDE.md)
- [سجل التغييرات](CHANGELOG.md)

---
صنع بـ ❤️ للمجتمع العربي

ذكاء اصطناعي العرب ⚡️
https://t.me/AI4Arabs
الجروب الخاص بالقناة 
المنتدى التفاعلي - AI4Arabs. ☝️
https://t.me/AI_FOR_ARAB
مجموعة : 
مجتمع رواد الذكاء الاصطناعي🤩
https://t.me/Shawxvip2
