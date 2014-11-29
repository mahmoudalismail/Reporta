import tornado.ioloop
import tornado.web
import tornado.escape
from EchoHandler import EchoHandler
from IntentHandler import IntentHandler

def get_app():
    return tornado.web.Application([
        (r'/echo', EchoHandler),
        (r'/', IntentHandler)
    ], debug=True)

def main():
    application = get_app()
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
