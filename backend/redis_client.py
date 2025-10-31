import redis
import os

REDIS_HOST = os.getenv("REDIS_HOST", "LocalHost") 
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
redis_client = redis.from_url(REDIS_URL, decode_responses=True)

print("Redis client configured.")


def get_redis_client():
    return redis_client


