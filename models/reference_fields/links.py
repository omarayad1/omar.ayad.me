import datetime
from flask.ext.mongoengine import MongoEngine

db = MongoEngine()

class Links(db.Document):
	link=db.URLField()