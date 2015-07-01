from flask.views import MethodView
from flask import render_template
from helpers import markdown_converter
import models

class ProjectsController(MethodView):
	def get(self,id):
		if id is None:
			data_projects = models.projects.Projects.objects
			return render_template('projects.html', data=data_projects)
		else:
			data = models.projects.Projects.objects(pk=id).first()
			md = []
			for el in data.markdown:
				html = markdown_converter.convert(el.markdown)
				md.append(html)
			return render_template('project.html', item=data, markdown=md)
