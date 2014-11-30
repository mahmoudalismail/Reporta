import tornado.testing
import tornado.httputil

import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import server

class IntentsTests(tornado.testing.AsyncHTTPTestCase):
    def get_app(self):
        return server.get_app()

    @tornado.testing.gen_test
    def start(self):
        mock_outcome = {
            "id": "absc0sasdadsaf",
            "intent" : "start",
            "user": "Hey Reporta",
            "reporta": "Hi John. How are you today?"
        }
        response = yield self.http_client.fetch(self.get_url("/"),
                                                method="POST",
                                                headers=tornado.httputil.HTTPHeaders({"content-type": "application/json"}),
                                                body=tornado.escape.json_encode(mock_outcome))
        payload = tornado.escape.json_decode(response.body)
        self.assertEqual(payload["status"], 200)
        self.assertTrue("?" in payload["read"])

    @tornado.testing.gen_test
    def confirm_action(self):
        mock_outcome = {
            "id": "asdfjasdfsa",
            "intent" : "start",
        }
        yield self.http_client.fetch(self.get_url("/"),
                                                method="POST",
                                                headers=tornado.httputil.HTTPHeaders({"content-type": "application/json"}),
                                                body=tornado.escape.json_encode(mock_outcome))
        mock_outcome = {
          "id": "asdfjasdfsa",
          "_text" : "Yes",
          "intent" : "confirm_action",
          "entities" : { },
          "confidence" : 0.327
        }
        response = yield self.http_client.fetch(self.get_url("/"),
                                                method="POST",
                                                headers=tornado.httputil.HTTPHeaders({"content-type": "application/json"}),
                                                body=tornado.escape.json_encode(mock_outcome))
        payload = tornado.escape.json_decode(response.body)
        self.assertEqual(payload["status"], 200)
        print(payload["read"])
        self.assertTrue(len(payload["read"]) > 0)
        self.assertTrue("?" in payload["read"])

    @tornado.testing.gen_test
    def get_headlines(self):
        mock_outcome = {
            "id": "98ds314981321",
            "_text" : "Whats happening today?",
            "intent" : "get_headlines",
            "entities" : { },
            "confidence" : 0.525
        }
        response = yield self.http_client.fetch(self.get_url("/"),
                                                method="POST",
                                                headers=tornado.httputil.HTTPHeaders({"content-type": "application/json"}),
                                                body=tornado.escape.json_encode(mock_outcome))
        payload = tornado.escape.json_decode(response.body)
        self.assertEqual(payload["status"], 200)
        self.assertTrue(len(payload["read"]) > 0)
        self.assertTrue("?" in payload["read"])

    @tornado.testing.gen_test
    def get_headlines_topic(self):
        mock_outcome = {
            "id": "sadflkja098wf3j2f",
            "_text" : "Is there any news about pope?",
            "intent" : "get_headlines",
            "entities" : {
              "topic" : [ {
                "value" : "pope"
              } ]
            },
            "confidence" : 0.855
        }
        response = yield self.http_client.fetch(self.get_url("/"),
                                                method="POST",
                                                headers=tornado.httputil.HTTPHeaders({"content-type": "application/json"}),
                                                body=tornado.escape.json_encode(mock_outcome))
        payload = tornado.escape.json_decode(response.body)
        self.assertEqual(payload["status"], 200)
        self.assertTrue(len(payload["read"]) > 0)
        self.assertTrue("?" in payload["read"])
        self.assertTrue("pope" in payload["read"].lower())

    #@tornado.testing.gen_test
    #def get_summary(self):
        #mock_outcome = {
            #"id": "98ds314981321",
            #"_text" : "Whats happening today?",
            #"intent" : "get_headlines",
            #"entities" : { },
            #"confidence" : 0.525
        #}
        #response = yield self.http_client.fetch(self.get_url("/"),
                                                #method="POST",
                                                #headers=tornado.httputil.HTTPHeaders({"content-type": "application/json"}),
                                                #body=tornado.escape.json_encode(mock_outcome))
        #mock_summary = {
            #"id": "98ds314981321",
            #"_text" : "",
            #"intent" : "get_headlines",
            #"entities" : { },
            #"confidence" : 0.525
        #}
        #payload = tornado.escape.json_decode(response.body)
        #self.assertEqual(payload["status"], 200)
        #self.assertTrue("john" in payload["read"])

