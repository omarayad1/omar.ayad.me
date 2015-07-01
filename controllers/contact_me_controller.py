from flask.views import MethodView
from flask import render_template

class ContactMeController(MethodView):
	def get(self):
		return render_template('contact.html')