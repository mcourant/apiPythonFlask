from flask_restful import Resource, abort, request
from common.dbHandler import connection
from functools import wraps

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(func, 'authenticated', True):
            return func(*args, **kwargs)

        auth_token = request.headers.get('Auth-Token')
        acct = authToken(auth_token)

        if acct:
            return func(*args, **kwargs)

        abort(401)
    return wrapper

def authToken(auth_token):
    c, conn = connection()
    result = False
    c.execute('select api_key from db.api')
    r = c.fetchall()
    for rest in r:
        if rest["api_key"] == auth_token:
            result = True
    return result


class Resource(Resource):
    method_decorators = [authenticate]