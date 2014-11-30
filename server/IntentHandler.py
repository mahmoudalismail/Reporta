import tornado.escape
import tornado.web
import tornado.gen
from fuzzywuzzy import process
from RedisClient import RedisClient
from NYTimes import NYTimes
from phrases import *
from NLPParser import NLPParser

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

        if ("name" in self.outcome):
            self.name = self.outcome["name"]
        else:
            self.name = None

        if (intent == "start"):
            self.start()
        elif (intent == "confirm_action"):
            self.confirm_action()
        elif (intent == "get_headlines"):
            self.get_headlines()
        elif (intent == "get_summary"):
            self.get_summary()
        elif (intent == "get_media"):
            self.get_media()
        elif (intent == "save_headline"):
            self.save_headline()
        else:
            self.error_response("No recognizable intent found")

    def start(self):
        r = RedisClient()

        # Clear the state for this new user
        r.set(self._id + ":state", None)
        r.set(self._id + ":articles", None)
        r.set(self._id + ":selected", None)

        NYTimes.get_headlines(self.respond_start)

    def respond_start(self, articles):
        r = RedisClient()
        keywords = r.get(self._id + ":keywords")

        if keywords:
            keyword_articles = NYTimes.check_keywords(articles, keywords)
            hasUpdate = len(keywords) > 0
            articles = keyword_articles
        else:
            hasUpdate = False

        start_state = UpdatesOrNoUpdates(hasUpdate, self.name)
        self.payload = {
            "read": start_state.get_phrase()
        }
        r.set(self._id + ":articles", articles)
        r.set(self._id + ":state", "start")
        self.finish_response()

    def confirm_action(self):
        r = RedisClient()
        current_state = r.get(self._id + ":state")

        if (current_state != "start"):
            self.error_response("Sorry, what are you saying okay for?")
        else:
            articles = r.get(self._id + ":articles")
            self.respond_get_headlines(articles)

    def get_headlines(self):
        topic = None
        if "entities" in self.outcome and\
            "topic" in self.outcome["entities"] and\
            "value" in self.outcome["entities"]["topic"][0]:
                topic = self.outcome["entities"]["topic"][0]["value"]
        NYTimes.get_headlines(self.respond_get_headlines, topic=topic)


    def respond_get_headlines(self, payload):
        sentence_headlines, topic_headlines, article_order = NLPParser.parse_headlines(map(lambda x: x["headline"], payload))

        found = FoundHeadlines(sentence_headlines, topic_headlines, self.name)
        self.payload = {
            "read": found.get_phrase()
        }

        r = RedisClient()

        ordered_articles = map(lambda x: payload[x], article_order)

        # State transition
        r.set(self._id + ":selected", None)
        r.set(self._id + ":articles", ordered_articles)
        r.set(self._id + ":state", "headlines")
        self.finish_response()

    # Picks an article given entities
    def extract_article(self):
        r = RedisClient()
        articles = r.get(self._id + ":articles")
        selected = r.get(self._id + ":selected")

        article = None

        entities = self.outcome["entities"]
        if "ordinal" in entities:
            value = entities["ordinal"][0]["value"]
            if value < len(articles):
                article = articles[value - 1]
        if not article and "topic" in entities:
            topic = entities["topic"][0]["value"]
            is_current_context = False
            for word in ["it", "this", "article"]:
                if word in topic:
                    article = selected
                    is_current_context = True
                    break
            if not is_current_context:
                # fuzzy string matching
                result = process.extractOne(topic, map(lambda x: x["headline"], articles))
                if (result[1] > 75):
                    for i, article_candidate in enumerate(articles):
                        if (article_candidate["headline"] == result[0]):
                            article = article_candidate
                            break
        if not article and selected:
            article = selected
        return article


    def get_summary(self):
        r = RedisClient()
        article = self.extract_article()
        if article:
            r.set(self._id + ":selected", article)
            self.payload = {
                "read": "%s. Would you like me to send the full article to your kindle?" % article["snippet"]
            }
            self.finish_response()
        else:
            self.error_response("Sorry I don't know what article you are talking about")

    def get_media(self):
        r = RedisClient()
        article = self.extract_article()
        if article:
            if article['multimedia']:
                r.set(self._id + ":selected", article)
                self.payload = {
                    "read": "%s" % article['multimedia'] # usable url for html
                }
                self.finish_response()
            else:
                self.error_response("Sorry I don't have images for that article")
        else:
            self.error_response("Sorry I don't know what article you are talking about")


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
