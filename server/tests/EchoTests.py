import tornado.testing
import tornado.httputil

import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import server

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
