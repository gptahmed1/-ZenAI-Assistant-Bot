import logging
from functools import wraps
from typing import Callable
import asyncio

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('bot.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def rate_limit(calls: int, period: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        last_reset = 0
        calls_made = 0
        
        @wraps(func)
        async def wrapper(*args, **kwargs):
            nonlocal last_reset, calls_made
            now = asyncio.get_event_loop().time()
            
            if now - last_reset >= period:
                calls_made = 0
                last_reset = now
            
            if calls_made >= calls:
                raise Exception("Rate limit exceeded")
            
            calls_made += 1
            return await func(*args, **kwargs)
        return wrapper
    return decorator
