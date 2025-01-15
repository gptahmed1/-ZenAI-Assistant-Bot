from cachetools import TTLCache, LRUCache
from typing import Optional

class CacheManager:
    def __init__(self, ttl: int, maxsize: int):
        self.message_cache = TTLCache(maxsize=maxsize, ttl=ttl)
        self.user_cache = LRUCache(maxsize=maxsize)
    
    def get_cached_response(self, key: str) -> Optional[str]:
        return self.message_cache.get(key)
    
    def cache_response(self, key: str, response: str):
        self.message_cache[key] = response
    
    def clear_cache(self):
        self.message_cache.clear()
        self.user_cache.clear()