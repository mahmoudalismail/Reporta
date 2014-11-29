import tornado.escape
import tornado.web

class EchoHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(tornado.escape.json_encode({
            "status": 200,
            "data": "Hello World"
        }))

    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        self.write(tornado.escape.json_encode({
            "status": 200,
            "data": data
        }))
