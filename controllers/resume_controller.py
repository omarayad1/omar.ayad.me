from flask.views import MethodView
from flask import render_template

class ResumeController(MethodView):
	def get(self):
		return render_template('resume.html')