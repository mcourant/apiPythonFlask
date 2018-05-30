from flask_restful import Resource

class UserDao(object):
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

        # This field will not be sent in the response
        self.status = 'active'