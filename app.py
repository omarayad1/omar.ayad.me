from flask import Flask, render_template
from controllers import home_controller
from controllers import background_controller
from controllers import about_controller
from controllers import projects_controller
from controllers import resume_controller
from controllers import contact_me_controller
from controllers import sitemap_controller
from flask.ext.mongoengine import MongoEngine
from helpers import assets_pipeline
import logging
import sys
import os

db = MongoEngine()

app = Flask(__name__)


# Adjusting logging settings to dev
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

# routes

app.add_url_rule('/', view_func=home_controller.HomeController.as_view('home'))
app.add_url_rule('/bgcolor', view_func=background_controller.BackgroundController.as_view('bg'))
app.add_url_rule('/about', view_func=about_controller.AboutController.as_view('about'))

projects_view = projects_controller.ProjectsController.as_view('projects')

app.add_url_rule('/projects/',
	defaults={'id': None},
	view_func=projects_view,
	methods=['GET',])

app.add_url_rule('/projects/<id>',
	view_func=projects_view,
	methods=['GET',])

app.add_url_rule('/resume', view_func=resume_controller.ResumeController.as_view('resume'))
app.add_url_rule('/contact', view_func=contact_me_controller.ContactMeController.as_view('contact'))
app.add_url_rule('/sitemap.xml', view_func=sitemap_controller.SitemapController.as_view('sitemap'))

# error Handling

@app.errorhandler(404)
def page_not_found(e):
	return render_template('error/404.html'), 404

if __name__ == "__main__":
    app.run(debug=True,port=int(os.environ.get('PORT', 5000)))
