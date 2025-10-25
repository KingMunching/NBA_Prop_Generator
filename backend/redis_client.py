import redis
import os

REDIS_HOST = os.getenv("REDIS_HOST", "LocalHost") 
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT,db=0, decode_responses=True)

def get_redis_client():
    return redis_client


