import tornado.testing
import server
import unittest

class EchoTests(tornado.testing.AsyncHTTPTestCase):
    def get_app(self):
        return server.get_app()

    def test_homepage(self):
        self.assertEqual(True, True)

def all():
    suite = unittest.TestSuite()
    suite.addTest(EchoTests("test_homepage"))
    return suite

def main():
    tornado.testing.main()

if __name__ == "__main__":
    main()
