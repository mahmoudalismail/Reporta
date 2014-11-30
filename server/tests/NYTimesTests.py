import tornado.testing
import tornado.httputil

import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from NYTimes import NYTimes

class NYTimesTests(tornado.testing.AsyncTestCase):
    def cb(self, payload):
        print 1
        print payload
        self.assertTrue(len(payload) > 0)
        self.assertTrue("snippet" in payload[0])
        self.assertTrue("multimedia" in payload[0])
        self.assertTrue("abstract" in payload[0])
        self.assertTrue("keywords" in payload[0])
        self.stop()

    def get_headlines(self):
        NYTimes.get_headlines(self.cb)
        self.wait()
