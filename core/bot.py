import google.generativeai as genai
from telebot.async_telebot import AsyncTeleBot
from config.settings import Config
from utils.security import SecurityManager
from utils.cache import CacheManager
from utils.helpers import setup_logging, rate_limit
import asyncio
from typing import Optional

logger = setup_logging()

class AIBot:
    def __init__(self):
        self.config = Config()
        self.security = SecurityManager()
        self.cache = CacheManager(
            ttl=self.config.CACHE_TTL,
            maxsize=self.config.CACHE_MAX_SIZE
        )
        
        self.bot = AsyncTeleBot(self.config.TELEGRAM_TOKEN)
        
        # تهيئة Google AI
        genai.configure(api_key=self.config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(
            model_name="gemini-pro",
            generation_config={
                "temperature": self.config.AI_TEMPERATURE,
                "top_p": self.config.AI_TOP_P,
                "top_k": self.config.AI_TOP_K,
                "max_output_tokens": self.config.AI_MAX_TOKENS,
            }
        )
        
        self.setup_handlers()

    def setup_handlers(self):
        @self.bot.message_handler(commands=['start'])
        @rate_limit(calls=5, period=60)
        async def send_welcome(message):
            try:
                welcome_text = (
                    "👋 *مرحباً بك في المساعد الذكي!*\n\n"
                    "🤖 أنا هنا لمساعدتك في أي سؤال أو استفسار.\n"
                    "💡 يمكنك سؤالي عن أي شيء وسأحاول مساعدتك.\n\n"
                    "📝 *الأوامر المتاحة:*\n"
                    "/start - بدء محادثة جديدة\n"
                    "/help - عرض المساعدة\n"
                    "/reset - إعادة تعيين المحادثة"
                )
                await self.bot.reply_to(
                    message,
                    welcome_text,
                    parse_mode='Markdown'
                )
            except Exception as e:
                logger.error(f"Error in welcome: {str(e)}")
                await self.handle_error(message)

        @self.bot.message_handler(commands=['help'])
        async def send_help(message):
            help_text = (
                "🔍 *كيفية استخدام البوت:*\n\n"
                "1. اكتب سؤالك بشكل واضح\n"
                "2. انتظر الرد\n"
                "3. يمكنك متابعة المحادثة بشكل طبيعي\n\n"
                "⚠️ *ملاحظات:*\n"
                "• حد الرسائل: 30 رسالة/دقيقة\n"
                "• الحد الأقصى للرسالة: 4096 حرف"
            )
            await self.bot.reply_to(
                message,
                help_text,
                parse_mode='Markdown'
            )

        @self.bot.message_handler(commands=['reset'])
        async def reset_chat(message):
            try:
                self.cache.clear_cache()
                await self.bot.reply_to(
                    message,
                    "✨ *تم إعادة تعيين المحادثة!*",
                    parse_mode='Markdown'
                )
            except Exception as e:
                logger.error(f"Error in reset: {str(e)}")
                await self.handle_error(message)

        @self.bot.message_handler(func=lambda message: True)
        @rate_limit(calls=self.config.RATE_LIMIT_MESSAGES, period=self.config.RATE_LIMIT_PERIOD)
        async def handle_message(message):
            try:
                async with asyncio.timeout(30):
                    await self._process_message(message)
            except asyncio.TimeoutError:
                await self.bot.reply_to(
                    message,
                    "⚠️ *العملية استغرقت وقتاً طويلاً*",
                    parse_mode='Markdown'
                )
            except Exception as e:
                logger.error(f"Error processing message: {str(e)}")
                await self.handle_error(message)

    async def _process_message(self, message):
        user_input = message.text.strip()

        if not self._validate_input(user_input):
            await self.bot.reply_to(
                message,
                "⚠️ *الرجاء إدخال نص صالح*",
                parse_mode='Markdown'
            )
            return

        typing_msg = await self.bot.send_message(
            message.chat.id,
            "🤔 *جاري التفكير...*",
            parse_mode='Markdown'
        )

        try:
            # التحقق من الذاكرة المؤقتة
            cache_key = self.security.hash_message(user_input)
            response_text = self.cache.get_cached_response(cache_key)

            if not response_text:
                # الحصول على رد من AI
                ai_response = await asyncio.to_thread(
                    self.model.generate_content,
                    user_input
                )
                response_text = ai_response.text
                self.cache.cache_response(cache_key, response_text)

            # تنسيق الرد
            formatted_response = self._format_response(response_text)
            
            # حذف رسالة "جاري التفكير"
            await self.bot.delete_message(
                message.chat.id,
                typing_msg.message_id
            )
            
            # إرسال الرد
            await self.bot.reply_to(
                message,
                formatted_response,
                parse_mode='Markdown'
            )

        except Exception as e:
            logger.error(f"Error in AI processing: {str(e)}")
            await self.handle_error(message)

    def _validate_input(self, text: str) -> bool:
        return bool(text and len(text.strip()) > 0 and 
                   len(text) < self.config.MAX_MESSAGE_LENGTH)

    def _format_response(self, text: str) -> str:
        lines = text.split('\n')
        formatted_lines = []
        for line in lines:
            line = line.strip()
            if line.startswith(('•', '-', '*')):
                formatted_lines.append(f"• {line[1:].strip()}")
            else:
                formatted_lines.append(line)
        return '\n'.join(formatted_lines)

    async def handle_error(self, message):
        await self.bot.reply_to(
            message,
            "⚠️ *عذراً، حدث خطأ. الرجاء المحاولة مرة أخرى.*",
            parse_mode='Markdown'
        )

    async def run(self):
        """تشغيل البوت"""
        try:
            logger.info("Starting bot...")
            while True:
                try:
                    await self.bot.polling(non_stop=True, timeout=60)
                except Exception as e:
                    logger.error(f"Polling error: {str(e)}")
                    await asyncio.sleep(5)
        except Exception as e:
            logger.critical(f"Bot crashed: {str(e)}")
