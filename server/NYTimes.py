import tornado.httpclient
import tornado.gen
import test_nyt_api
import random

class NYTimes():

    @staticmethod
    @tornado.gen.coroutine
    def get_headlines(callback, topic=None, keywords=None):
        #if there is a topic, search about that topic
        #none topic is general headline using previous keywords used
        payload = []
        isUpdate = False
        if topic:
            specific_articles = test_nyt_api.get_5_specific(topic)
            if specific_articles:
                for art in specific_articles:
                    clean_art = test_nyt_api.clean_entry(art) 
                    payload.append(test_nyt_api.clean_entry(art))


        else:
            isUpdate = True
            general_article = test_nyt_api.get_general()
            if general_article:
                for art in general_article:
                    clean_art = test_nyt_api.clean_entry(art)
                    payload.append(test_nyt_api.clean_entry(art))

        print payload


        client = tornado.httpclient.AsyncHTTPClient()
        response = yield client.fetch("http://google.com")
        callback(payload,isUpdate)




# here on are test methods

def callback(payload):
    print payload

def main():

    topic = 'Obama'
    NYTimes.get_headlines(callback, topic)


if __name__ == "__main__":
    main()

