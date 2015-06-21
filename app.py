from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine
from helpers import assets_pipeline, markdown_converter, random_color_gen
from models import about, projects
import logging
import sys
import os

db = MongoEngine()

app = Flask(__name__)


# Setting logging settings to dev
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.INFO)

# Configuring DB

app.config['MONGODB_SETTINGS'] = {
	'host': os.environ['MONGOLAB_URI']
}

db.init_app(app)
# building and compressing assets
env = assets_pipeline.load_paths(app)
env = assets_pipeline.register_js_components(env)
env = assets_pipeline.register_css_components(env)

@app.route("/", methods=['GET'])
def index():
	return render_template('index.html')


@app.route("/bgcolor", methods=['GET'])
def get_background_color():
	return random_color_gen.gen()


@app.route("/about", methods=['GET'])
def about_me():
	data_about = about.About.objects
	return render_template('about.html', data=data_about)


@app.route("/projects", methods=['GET'])
def projects_all():
	data_projects = projects.Projects.objects
	return render_template('projects.html', data=data_projects)

@app.route("/projects/<id>", methods=['GET'])
def projects_item(id):
	data = projects.Projects.objects(pk=id).first()
	md = []
	for el in data.markdown:
		html = markdown_converter.convert(el.markdown)
		md.append(html)
	return render_template('project.html', item=data, markdown=md)


@app.route("/resume", methods=['GET'])
def get_resume():
	return render_template('resume.html')

@app.route("/contact", methods=['GET'])
def get_contact_me():
	return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True,port=int(os.environ.get('PORT', 5000)))
