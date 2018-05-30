from flask_restful import fields, marshal_with
from resources.users.userHandler import getUsers, postUser
from common.authentificate import Resource

resource_fields = {
    'id':   fields.String,
    'name':    fields.String,
    'email':    fields.String
}

class Users(Resource):
	@marshal_with(resource_fields)
	def get(self):
		return getUsers()
	@marshal_with(resource_fields)
	def post(self):
		return postUser()