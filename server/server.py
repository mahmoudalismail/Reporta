import tornado.ioloop
import tornado.web
import tornado.escape
from EchoHandler import EchoHandler
from IntentHandler import IntentHandler
import os

def get_app():
    return tornado.web.Application([
        (r'/echo', EchoHandler),
        (r'/', IntentHandler)
    ], debug=True)

def main():
    port = int(os.environ.get("PORT", 5000))
    application = get_app()
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
