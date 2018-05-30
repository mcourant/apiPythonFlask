from flask import Flask
from flask_restful import Api
from resources.users.user import Users

app = Flask(__name__)
api = Api(app)

api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')