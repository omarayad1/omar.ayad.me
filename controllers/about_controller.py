from flask.views import MethodView
from flask import render_template
from models import about

class AboutController(MethodView):
	def get(self):
		data_about = about.About.objects
		return render_template('about.html', data=data_about)
