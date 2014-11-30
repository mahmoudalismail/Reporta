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
        if (intent == "start"):
            self.start()
        elif (intent == "confirm"):
            self.confirm()
        elif (intent == "get_headlines"):
            self.get_headlines()
        elif (intent == "get_summary"):
            self.get_summary()
        elif (intent == "get_media"):
            pass
        elif (intent == "save_headline"):
            pass
        else:
            self.error_response("No recognizable intent found")

    def start(self):
        NYT.get_headlines(self.respond_start)
        r = RedisClient()

        # Clear the state for this new user
        r.set(self._id + ":state", None)
        r.set(self._id + ":articles", None)
        r.set(self._id + ":selected", None)

    def respond_start(self, payload):
        self.payload = {
            read: "I have 5 updates on stories you're following. Would you like to hear them?"
        }
        r.set(self._id + ":articles", payload)
        r.set(self._id + ":state", "start")
        self.finish_response()

    def confirm(self):
        r = RedisClient()
        current_state = r.get(self._id + ":state")
        if (current_state != "start"):
            self.error_response("Sorry, what are you saying okay for?")
        else:
            articles = r.get(self._id + ":articles")
            respond_get_headlines(articles)

    def get_headlines(self):
        NYTimes.get_headlines(self.respond_get_headlines)

    def respond_get_headlines(self, payload):
        self.payload = {
            "read": "Your articles today are: %s" % payload[0]
        }
        r = RedisClient()

        # State transition
        r.set(self._id + ":selected", None)
        r.set(self._id + ":articles", payload)
        r.set(self._id + ":state", "headlines")
        self.finish_response()

    @tornado.web.asynchronous
    def get_summary(self):
        number_words = ["first", "second", "third", "fourth", "fifth", "sixth",
                        "seventh", "eigth", "ninth", "tenth"]
        r = RedisClient()
        articles = r.get(self._id + ":articles")
        entities = self.outcome["entities"]
        article = None
        if "topic" in entities:
            topic = entities["topic"]
            for article in articles:
                if topic in article:
                    article = article
                    break
        elif "nArticle" in entities:
            nArticle = entities["nArticle"]
            for i, number_word in enumerate(number_words):
                if number_word in nArticle:
                    if len(articles) >= i:
                        article = articles[i]
        if article:
            NYTimes.get_summary(article)
            r.set(self._id + ":currentArticle", article)
        else:
            self.payload = {
                "read": "Sorry, I didn't understand that"
            }
            self.finish_response()

    def respond_get_summary(self, summary):
        self.payload = {
            "read": summary
        }
        self.finish_response()

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
