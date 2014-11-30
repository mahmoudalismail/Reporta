import tornado.ioloop
import tornado.web
import tornado.escape
import os
from NLPParser import NLPParser

from EchoHandler import EchoHandler
from IntentHandler import IntentHandler

# First initialization will cause NLP
# data to be built
print "Building NLP..."
NLPParser.build()
print "Building NLP done"

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
