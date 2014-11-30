import tornado.testing
import unittest
from RedisTests import RedisTests
from EchoTests import EchoTests
from IntentsTests import IntentsTests
from NYTimesTests import NYTimesTests

def all():
    suite = unittest.TestSuite()
    suite.addTest(EchoTests("get"))
    suite.addTest(EchoTests("post"))
    suite.addTest(RedisTests("set_and_get"))
    suite.addTest(NYTimesTests("get_headlines"))
    suite.addTest(IntentsTests("start"))
    suite.addTest(IntentsTests("confirm_action"))
    suite.addTest(IntentsTests("get_headlines"))
    suite.addTest(IntentsTests("get_headlines_topic"))
    suite.addTest(IntentsTests("get_summary"))
    suite.addTest(IntentsTests("get_media"))
    return suite

def main():
    tornado.testing.main()

if __name__ == "__main__":
    main()
