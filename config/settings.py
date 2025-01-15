import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    
    # محددات الاستخدام
    MAX_MESSAGE_LENGTH = 4096
    RATE_LIMIT_MESSAGES = 30
    RATE_LIMIT_PERIOD = 60
    
    # إعدادات الذاكرة المؤقتة
    CACHE_TTL = 3600
    CACHE_MAX_SIZE = 1000
    
    # إعدادات AI
    AI_TEMPERATURE = 0.9
    AI_TOP_P = 0.95
    AI_TOP_K = 64
    AI_MAX_TOKENS = 8192
