import tornado.ioloop
import tornado.web

class HelloWorldHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")


application = tornado.web.Application([
    (r'/', HelloWorldHandler)
])

def main():
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
