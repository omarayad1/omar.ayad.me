import datetime
from flask.ext.mongoengine import MongoEngine
from reference_fields import links, technologies, markdown_file


db = MongoEngine()

class Projects(db.Document):
	name = db.StringField()
	link = db.ReferenceField(links.Links)
	github = db.ListField(db.ReferenceField(links.Links))
	technologies= db.ListField(db.ReferenceField(technologies.Technologies))
	description = db.StringField()
	markdown = db.ListField(db.ReferenceField(markdown_file.MarkdownFile))