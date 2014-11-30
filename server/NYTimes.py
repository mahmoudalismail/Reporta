import tornado.httpclient
import tornado.gen
import test_nyt_api
import random

class NYTimes():
    @staticmethod
    @tornado.gen.coroutine
    def get_headlines(callback, topic=None, keywords=None):
        #if there is a topic, search about that topic
        # none topic is general headline using previous keywords used
        #else, newest headlines
        payload = []
        isUpdate = False

        if topic:
            specific_articles = test_nyt_api.get_5_specific(topic)
            if specific_articles:
                for art in specific_articles:
                    clean_art = test_nyt_api.clean_entry(art)
                    payload.append(test_nyt_api.clean_entry(art))

        else:
            general_article = test_nyt_api.get_general()
            if general_article:
                for art in general_article:
                    clean_art = test_nyt_api.clean_entry(art)
                    payload.append(test_nyt_api.clean_entry(art))

        callback(payload)

    @staticmethod
    def check_keywords(articles, keywords):
        key_set = set(keywords)
        accepted = []
        for article in articles:
            for keyword in article["keyword"]:
                if keyword in key_set:
                    accepted.append(article)
                    break
        return accepted

