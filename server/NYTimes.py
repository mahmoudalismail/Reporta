import tornado.httpclient
import tornado.gen
import test_nyt_api
import random

class NYTimes():
    @staticmethod
    def get_headlines(callback, topic=None):
        #if there is a topic, search about that topic
        # none topic is general headline using previous keywords used
        #else, newest headlines
        if topic:
            test_nyt_api.get_articles(callback, topic = topic, limit = 5)
        else:
            test_nyt_api.get_articles(callback, limit = 5)

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

def cb(payload):
    print payload

def main():
    NYTimes.get_headlines(cb, topic="Obama")

if __name__ == "__main__":
    main()
