import tornado.ioloop
import tornado.web
import tornado.escape
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
client_path = os.path.join(parentdir, "client-web")

from NLPParser import NLPParser

from EchoHandler import EchoHandler
from IntentHandler import IntentHandler

from FileHandler import FileHandler

# Load NLP class
NLPParser.load()

def get_app():
    print client_path
    return tornado.web.Application([
        (r'/echo', EchoHandler),
        (r'/api', IntentHandler),
        (r'/', FileHandler, {"path": os.path.join(client_path, "index.html")}),
        (r'/(.*)', tornado.web.StaticFileHandler, {"path": client_path})
    ], debug=True)

def main():
    port = int(os.environ.get("PORT", 5000))
    application = get_app()
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
