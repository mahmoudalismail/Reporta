import tornado.testing
import tornado.httputil
import server
import unittest

class EchoTests(tornado.testing.AsyncHTTPTestCase):
    def get_app(self):
        return server.get_app()

    @tornado.testing.gen_test
    def get(self):
        response = yield self.http_client.fetch(self.get_url("/echo"))
        payload = tornado.escape.json_decode(response.body)
        self.assertEqual(payload["status"], 200)
        self.assertEqual(payload["data"], "Hello World")

    @tornado.testing.gen_test
    def post(self):
        data = {"test": "result"}
        response = yield self.http_client.fetch(self.get_url("/echo"),
                                                method="POST",
                                                headers=tornado.httputil.HTTPHeaders({"content-type": "application/json"}),
                                                body=tornado.escape.json_encode(data))
        payload = tornado.escape.json_decode(response.body)
        self.assertEqual(payload["data"], data)

def all():
    suite = unittest.TestSuite()
    suite.addTest(EchoTests("get"))
    suite.addTest(EchoTests("post"))
    return suite

def main():
    tornado.testing.main()

if __name__ == "__main__":
    main()
