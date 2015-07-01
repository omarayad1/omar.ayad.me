from flask.views import MethodView
from flask import render_template

class SitemapController(MethodView):
	def get(self):
		return render_template('sitemap.xml')