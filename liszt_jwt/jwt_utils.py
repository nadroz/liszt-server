import jwt
import os


def decode(token):
    secret = os.environ['TOKEN_KEY']
    token = jwt.decode(token, secret)
    return token
