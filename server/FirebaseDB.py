from firebase import firebase

class FirebaseDB(object):
    _instance = None
    def __init__(self):
        if not FirebaseDB._instance:
            FirebaseDB._instance = firebase.FirebaseApplication('https://reporta-ajz.firebaseio.com', None)

    def post(self, user_id, data):
        return FirebaseDB._instance.post('/' + user_id, data)