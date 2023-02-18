import os

class AppConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    DB_PORT = os.environ.get('DB_PORT') or 27017
    DB_NAME = os.environ.get('DB_NAME') or 'user_auth'
    # PERMANENT_SESSION_LIFETIME = 5
    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesystem'
    SESSION_COOKIE_SAMESITE = "None"
    SESSION_COOKIE_SECURE = True
    # SESSION_MONGODB_DB = DB_NAME
    # SESSION_MONGODB_COLLECT = 'users'

