import tornado.ioloop
import tornado.web
import tornado.escape

class EchoHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(tornado.escape.json_encode({
            "status": 200,
            "data": "Hello World success"
        }))

    def post(self):
        data = tornado.escape.json_encode(self.request.body)
        self.write(tornado.escape.json_encode({
            "status": 200,
            "data": data
        }))

def get_app():
    return tornado.web.Application([
        (r'/echo', EchoHandler)
    ], debug=True)

def main():
    application = get_app()
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
