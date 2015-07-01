from flask.views import MethodView
from helpers import random_color_gen

class BackgroundController(MethodView):
	def get(self):
		return random_color_gen.gen()