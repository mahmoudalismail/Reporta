import redis

class RedisClient(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = redis.StrictRedis(host="localhost", port=6379, db=0)
        return cls._instance

    def get(self, value):
        return RedisClient._instance.get(value)

    def set(self, key, value):
        return RedisClient._instance.set(key, value)
