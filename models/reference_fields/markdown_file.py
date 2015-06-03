import datetime
from flask.ext.mongoengine import MongoEngine

db = MongoEngine()

class MarkdownFile(db.Document):
	markdown = db.FileField()
	html = db.FileField()