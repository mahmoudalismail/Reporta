class RegisterHandler(tornado.web.RequestHandler):
  def post(self):
    payload = {}
    data = tornado.escape.json_decode(self.request.body)
    user_id = data["id"]
    if ("name" not in data):
      payload = {"status": 500}
    else:
      user_name = data["name"]
      r = RedisClient()
      r.set(user_id + ":name", user_name)
      payload = {
        "id": user_id,
        "name": user_name,
        "status": 200
      }
    self.write(tornado.escape.json_encode(self.payload))
    self.finish_response()