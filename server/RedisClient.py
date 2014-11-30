import redis
import json

class RedisClient(object):
    _instance = None
    def __init__(self):
        if not RedisClient._instance:
            RedisClient._instance = redis.StrictRedis(host="localhost", port=6379, db=0)

    def get(self, key):
        value = RedisClient._instance.get(key)
        if value[0] == "[" or value[0] == "{":
            value = json.loads(value)
        return value

    def set(self, key, value):
        if type(value) == list or type(value) == dict:
            value = json.dumps(value)
        return RedisClient._instance.set(key, value)
