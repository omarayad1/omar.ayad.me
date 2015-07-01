from flask.views import MethodView
from flask import render_template
import models

class AboutController(MethodView):
	def get(self):
		data_about = models.about.About.objects
		return render_template('about.html', data=data_about)
