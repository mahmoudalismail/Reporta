import tornado.web
import tornado.escape
import os
import requests

class QueryHandler(tornado.web.RequestHandler):
  def post(self):
    payload = {}
    data = tornado.escape.json_decode(self.request.body)
    self.query = data["query"]
    self.id = data["id"]
    client = tornado.httpclient.AsyncHTTPClient()
    print "Sending to wit"
    self.write(tornado.escape.json_encode({"status": 200}))
    self.finish()
    response = client.fetch('https://api.wit.ai/message?v=20141129&q=' + tornado.escape.url_escape(self.query),
                            headers=tornado.httputil.HTTPHeaders({
                                "Authorization": "Bearer B3HHZMAR6LHITBHGW4MHDAAMBRREGCIN"
                            }),
                            callback=self.respond_query)

  def respond_query(self, response):
    data = tornado.escape.json_decode(response.body)
    payload = data["outcomes"][0]
    payload["id"] = self.id
    print "Sending noe"
    print tornado.escape.json_encode(payload)
    client = tornado.httpclient.AsyncHTTPClient()
    r = requests.post("http://104.131.102.192:81/api",
                      data=tornado.escape.json_encode(payload), headers={'content-type': 'application/json'})
    print r

  def forward_query(self, response):
    print response
    print response.body
    pass
