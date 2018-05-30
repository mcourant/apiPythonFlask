from resources.users.userDao import UserDao
from common.dbHandler import connection
import pymysql
from flask_restful import reqparse, abort

parser = reqparse.RequestParser()
parser.add_argument("email")

def getUsers():
	c, conn = connection()
	result = []
	c.execute('SELECT * FROM db.users')
	r = c.fetchall()
	c.close()
	for rest in r:
		result.append(UserDao(rest["id"], rest["firstname"], rest["email"]))
	return result

def postUser():
	args = parser.parse_args()
	c,conn = connection()
	try:
		c.execute("INSERT INTO db.users (email) VALUES ('"+ args["email"] +"') ")
		conn.commit()
	except pymysql.IntegrityError as error:
		code, message = error.args
		if code == 1062:
			abort(400, message="Duplicate entry")

	return UserDao("NULL", "NULL", args["email"])