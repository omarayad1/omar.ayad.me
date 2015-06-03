import datetime
from flask.ext.mongoengine import MongoEngine

db = MongoEngine()

class Technologies(db.Document):
	technology=db.StringField()