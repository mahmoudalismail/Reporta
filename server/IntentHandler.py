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
        elif (intent == "action"):
            self.action()

    def get_headlines(self):
        # stub
        NYTimes.get_headlines(self.finish_response)

    def action(self):
        # stub
        articles = []
        return articles

    def finish_response(self):
        self.payload["status"] = 200
        self.write(tornado.escape.json_encode(self.payload))
        self.finish()
