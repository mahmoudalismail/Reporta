import tornado.escape
import tornado.web
import tornado.gen
from NYTimes import NYTimes

class IntentHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self):
        self.outcome = tornado.escape.json_decode(self.request.body)
        intent = self.outcome["intent"]
        if (intent == "get_headlines"):
            self.get_headlines()
        elif (intent == "get_summary"):
            self.get_summary()
        elif (intent == ""):
            self.get()
        else:
            self.error_response("No recognizable intent found")

    def get_headlines(self):
        NYTimes.get_headlines(self.finish_response)

    def get_summary(self):
        entities["topic"]
        return articles

    def finish_response(self, payload):
        payload["status"] = 200
        self.write(tornado.escape.json_encode(payload))
        self.finish()

    def error_response(self, reason):
        payload = {
            "status": 500,
            "reason": reason
        }
        self.write(tornado.escape.json_encode(payload))
        self.finish()
