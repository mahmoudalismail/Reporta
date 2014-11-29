import tornado.httpclient
import tornado.gen

class NYTimes():
    @tornado.gen.coroutine
    def get_headlines(self, callback):
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield client.fetch("http://google.com")
        payload = {
            "headlines": ["john"]
        }
        callback(payload)




