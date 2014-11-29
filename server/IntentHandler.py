import tornado.escape
import tornado.web
import tornado.gen
from RedisClient import RedisClient
from NYTimes import NYTimes

class IntentHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self):
        self.payload = {}
        self.outcome = tornado.escape.json_decode(self.request.body)
        intent = self.outcome["intent"]
        if ("id" in self.outcome):
            self._id = self.outcome["id"]
        else:
            self.error_response("No id passed in outcome")
        if (intent == "get_headlines"):
            self.get_headlines()
        elif (intent == "get_summary"):
            self.get_summary()
        elif (intent == ""):
            self.get()
        else:
            self.error_response("No recognizable intent found")

    def get_headlines(self):
        NYTimes.get_headlines(self.respond_get_headlines)

    def respond_get_headlines(self, payload):
        self.payload = {
            "read": "Your articles today are: %s" % payload["headlines"][0]
        }
        r = RedisClient()
        r.set(self._id + ":" + "headlines", payload["headlines"])
        self.finish_response()

    def get_summary(self):
        if "topic" in entities:
            pass
        return articles

    def finish_response(self):
        self.payload["status"] = 200
        self.write(tornado.escape.json_encode(self.payload))
        self.finish()

    def error_response(self, reason):
        payload = {
            "status": 500,
            "reason": reason
        }
        self.write(tornado.escape.json_encode(payload))
        self.finish()
