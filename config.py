import os


#default config
class BaseConfig(object):
  DEBUG = False
  SECRET_KEY = os.environ['FLASK_INTRO_SECRET_KEY']
  SQLALCHEMY_DATABASE_URI = os.environ['FLASK_INTRO_DB']

class DevelopmentConfig(BaseConfig):
  DEBUG = True

class ProductionConfig (BaseConfig):
  DEBUG = False
