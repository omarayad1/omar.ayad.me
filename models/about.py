import datetime
from flask.ext.mongoengine import MongoEngine

db = MongoEngine()

class About(db.Document):
	title = db.StringField()
	description = db.StringField()
	bullets = db.ListField()