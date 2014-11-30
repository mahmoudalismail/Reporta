import tornado.httpclient
import tornado.gen

class NYTimes():
    @staticmethod
    @tornado.gen.coroutine
    def get_headlines(callback, topic=None, keywords=None):
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
