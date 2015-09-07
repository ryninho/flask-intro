import os


#default config
class BaseConfig(object):
  DEBUG = False
  SECRET_KEY = '\x98\x9f\x83\xff\xdd?\xaf\xb7\x9c\xfd)\x8b\xb0X\xe9y\r\x14A%\x17\x1a\xa5\xbd' # os.environ['FLASK_INTRO_SECRET_KEY']
  SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(BaseConfig):
  DEBUG = True

class ProductionConfig (BaseConfig):
  DEBUG = False
