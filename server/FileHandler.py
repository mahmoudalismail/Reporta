import tornado.web
import os

class FileHandler(tornado.web.StaticFileHandler):
    def initialize(self, path):
        self.dirname, self.filename = os.path.split(path)
        super(FileHandler, self).initialize(self.dirname)

    def get(self, path=None, include_body=True):
        # Ignore 'path'.
        super(FileHandler, self).get(self.filename, include_body)

