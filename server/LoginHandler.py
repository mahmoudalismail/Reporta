class LoginHandler(tornado.web.RequestHandler):
  def post(self):
    payload = {}
    data = tornado.escape.json_decode(self.request.body)
    user_id = data["id"]
    r = RedisClient()
    name = r.get(self._id + ":name")
    if not name:
      payload = {"status": 500}
    else:
      payload = {
        "id": user_id,
        "name": name,
        "status": 200
      }
    self.write(tornado.escape.json_encode(self.payload))
    self.finish_response()