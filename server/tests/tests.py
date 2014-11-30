import tornado.testing
import unittest
from RedisTests import RedisTests
from EchoTests import EchoTests
from IntentsTests import IntentsTests

def all():
    suite = unittest.TestSuite()
    suite.addTest(EchoTests("get"))
    suite.addTest(EchoTests("post"))
    suite.addTest(RedisTests("set_and_get"))
    suite.addTest(IntentsTests("get_headlines"))
    suite.addTest(IntentsTests("start"))
    return suite

def main():
    tornado.testing.main()

if __name__ == "__main__":
    main()
