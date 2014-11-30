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
        response = yield self.http_client.fetch(self.get_url("/api"),
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
        yield self.http_client.fetch(self.get_url("/api"),
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
        response = yield self.http_client.fetch(self.get_url("/api"),
                                                method="POST",
                                                headers=tornado.httputil.HTTPHeaders({"content-type": "application/json"}),
                                                body=tornado.escape.json_encode(mock_outcome))
        payload = tornado.escape.json_decode(response.body)
        self.assertEqual(payload["status"], 200)
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
        response = yield self.http_client.fetch(self.get_url("/api"),
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
            "_text" : "Is there any news about the pope?",
            "intent" : "get_headlines",
            "entities" : {
              "topic" : [ {
                "value" : "pope"
              } ]
            },
            "confidence" : 0.855
        }
        response = yield self.http_client.fetch(self.get_url("/api"),
                                                method="POST",
                                                headers=tornado.httputil.HTTPHeaders({"content-type": "application/json"}),
                                                body=tornado.escape.json_encode(mock_outcome))
        payload = tornado.escape.json_decode(response.body)
        self.assertEqual(payload["status"], 200)
        self.assertTrue(len(payload["read"]) > 0)
        self.assertTrue("?" in payload["read"])
        self.assertTrue("pope" in payload["read"].lower())

    @tornado.testing.gen_test
    def get_summary(self):
        mock_outcome = {
            "id": "safdsafsdf",
            "_text" : "Is there any news about the pope?",
            "intent" : "get_headlines",
            "entities" : {
              "topic" : [ {
                "value" : "pope"
              } ]
            },
            "confidence" : 0.855
        }
        response = yield self.http_client.fetch(self.get_url("/api"),
                                     method="POST",
                                     headers=tornado.httputil.HTTPHeaders({"content-type": "application/json"}),
                                     body=tornado.escape.json_encode(mock_outcome))
        payload = tornado.escape.json_decode(response.body)
        mock_outcome = {
            "id": "safdsafsdf",
            "_text" : "Tell me more about the third one",
            "intent" : "get_summary",
            "entities" : {
              "ordinal" : [ {
                "value" : 3
              } ],
              "topic" : [ {
                "value" : "one"
              } ]
            },
            "confidence" : 1.0
        }
        response = yield self.http_client.fetch(self.get_url("/api"),
                                                method="POST",
                                                headers=tornado.httputil.HTTPHeaders({"content-type": "application/json"}),
                                                body=tornado.escape.json_encode(mock_outcome))
        payload = tornado.escape.json_decode(response.body)
        self.assertEqual(payload["status"], 200)
        self.assertTrue(len(payload["read"]) > 0)
        mock_outcome =  {
            "id": "safdsafsdf",
            "_text" : "Tell me more about the pope",
            "intent" : "get_summary",
            "entities" : {
              "topic" : [ {
                "value" : "the pope"
              } ]
            },
            "confidence" : 0.928
        }
        response = yield self.http_client.fetch(self.get_url("/api"),
                                                method="POST",
                                                headers=tornado.httputil.HTTPHeaders({"content-type": "application/json"}),
                                                body=tornado.escape.json_encode(mock_outcome))
        payload = tornado.escape.json_decode(response.body)
        self.assertEqual(payload["status"], 200)
        self.assertTrue(len(payload["read"]) > 0)
        mock_outcome =  {
            "id": "safdsafsdf",
            "_text" : "Tell me more about it",
            "intent" : "get_summary",
            "entities" : {
              "topic" : [ {
                "value" : "it"
              } ]
            },
            "confidence" : 0.896
        }
        response = yield self.http_client.fetch(self.get_url("/api"),
                                                method="POST",
                                                headers=tornado.httputil.HTTPHeaders({"content-type": "application/json"}),
                                                body=tornado.escape.json_encode(mock_outcome))
        payload = tornado.escape.json_decode(response.body)
        self.assertEqual(payload["status"], 200)
        self.assertTrue(len(payload["read"]) > 0)
        
    @tornado.testing.gen_test
    def get_media(self):
        mock_outcome = {
            "id": "safdsafsdf",
            "_text" : "What are the headlines from France?",
            "intent" : "get_headlines",
            "entities" : {
              "topic" : [ {
                "value" : "France"
              } ]
            },
            "confidence" : 1.0
        }
        response = yield self.http_client.fetch(self.get_url("/api"),
                                     method="POST",
                                     headers=tornado.httputil.HTTPHeaders({"content-type": "application/json"}),
                                     body=tornado.escape.json_encode(mock_outcome))
        payload = tornado.escape.json_decode(response.body)
    
        mock_outcome =  {
            "id": "safdsafsdf",
            "_text" : "Get me images from the fourth article",
            "intent" : "get_media",
            "entities" : {
              "ordinal" : [ {
                "value" : 4
              } ]
            },
            "confidence" : 0.999
        }
        response = yield self.http_client.fetch(self.get_url("/api"),
                                                method="POST",
                                                headers=tornado.httputil.HTTPHeaders({"content-type": "application/json"}),
                                                body=tornado.escape.json_encode(mock_outcome))
        payload = tornado.escape.json_decode(response.body)
        self.assertEqual(payload["status"], 200)
        self.assertTrue(len(payload["read"]) > 0)
        self.assertTrue("http://www.nytimes.com/images" in payload["read"])
        self.assertFalse("thumbStandard.jpg" in payload["read"])

        mock_outcome =  {
            "id": "safdsafsdf",
            "_text" : "Get media about the second one",
            "intent" : "get_media",
            "entities" : {
              "ordinal" : [ {
                "value" : 2
              } ]
            },
            "confidence" : 0.999
        }
        response = yield self.http_client.fetch(self.get_url("/api"),
                                                method="POST",
                                                headers=tornado.httputil.HTTPHeaders({"content-type": "application/json"}),
                                                body=tornado.escape.json_encode(mock_outcome))
        payload = tornado.escape.json_decode(response.body)
        self.assertEqual(payload["status"], 200)
        self.assertTrue(len(payload["read"]) > 0)
        self.assertTrue("http://www.nytimes.com/images" in payload["read"])
        self.assertFalse("thumbStandard.jpg" in payload["read"])


