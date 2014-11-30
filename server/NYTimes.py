import tornado.httpclient
import tornado.gen
import test_nyt_api


class NYTimes():

    def __init__:
        self.recent_article_tuples = []
        #self.saved_articles = []

    def get_personal_keywords():
        spare_keywords = ['Al Jazeera', 'Russia', 'Water','Obama','Healthcare','Fire']
        keywords = []
        for art in self.recent_article_tuples.shuffle():
            keywords.append(art[0])
        for i in range (5-len(self.recent_article_tuples)):
            keywords.append(spare_keywords[i])
        return keywords

    @staticmethod
    @tornado.gen.coroutine
    def get_headlines(callback, topic=None, keywords=None):
        #if there is a topic, search about that topic
        #none topic is general headline using previous keywords used
    
        if topic:
            specific_articles = test_nyt_api.get_5_specific(topic)
            if specific_articles:
                for art in specific_articles:
                    self.recent_article_tuples.append((topic,test_nyt_api.clean_entry(art)))

        else:
            keywords = get_personal_keywords()
            personal_articles = test_nyt_api.get_5_personal()
            if personal_articles:
                for art in personal_articles:
                    self.recent_article_tuples.append((topic,test_nyt_api.clean_entry(art)))


        client = tornado.httpclient.AsyncHTTPClient()
        response = yield client.fetch("http://google.com")
        payload = ["john", "clare", "dogs", "cats"]
        callback(payload)

    @staticmethod
    @tornado.gen.coroutine
    def get_summary(article, callback):
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield client.fetch("http://google.com")
        payload = "John is a good man"
        callback(payload)


def main():
    recent_articles = []

    saved_articles = []

    keywords = ['Ferguson','Healthcare']

    # personal = get_5_personal()
    # for k in personal:
    #   new_print(k)
    # print("\n"*(10))


    specific = get_5_specific("Russia")
    for s in specific:
        new_print(s)


    
    


if __name__ == "__main__":
    main()

    s


