import redis
import unittest

class RedisTests(unittest.TestCase):
    def set_and_get(self):
        r = redis.StrictRedis(host="localhost", port=6379, db=0)
        r.set("foo", "bar")
        self.assertEqual(r.get("foo"), "bar")
