"""
This module is used to interact with a Redis database.

WARNING: This script will flush the entire Redis database. Use with caution.
"""
import redis

redis_client = redis.StrictRedis(host="0.0.0.0", port=6379, db=0, decode_responses=True)
redis_client.flushdb()
