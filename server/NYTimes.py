import tornado.httpclient
import tornado.gen

class NYTimes():
    @staticmethod
    @tornado.gen.coroutine
    def get_headlines(callback):
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield client.fetch("http://google.com")
        payload = {
            "headlines": ["john"]
        }
        callback(payload)




