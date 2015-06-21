import os

from flask.ext import assets

def load_paths(app):
    env = assets.Environment(app)
    env.load_path = [
            os.path.join(os.path.dirname(__file__), "../"),
            os.path.join(os.path.dirname(__file__), '../sass'),
            os.path.join(os.path.dirname(__file__), '../coffee'),
            os.path.join(os.path.dirname(__file__), '../bower_components')
    ]
    return env

def register_js_components(env):
    env.register(
            "js_all",
            assets.Bundle(
                "jquery/dist/jquery.min.js",
                "bootstrap/dist/js/bootstrap.min.js",
                "bootstrap/js/./alert.js",
                "bootstrap/js/./tooltip.js",
                "bootstrap/js/./scrollspy.js",
                "bootstrap/js/./transition.js",
                "bootstrap/js/./button.js",
                "bootstrap/js/./collapse.js",
                "bootstrap/js/./popover.js",
                "bootstrap/js/./affix.js",
                "bootstrap/js/./tab.js",
                "bootstrap/js/./dropdown.js",
                "bootstrap/js/./carousel.js",
                "bootstrap/js/modal.js",
                "markdown/lib/markdown.js",
                assets.Bundle(
                        'setBackgroundColor.coffee',
                        filters=['coffeescript']
                    ),
                output="js_all.js"
            )
    )
    return env


def register_css_components(env):
    env.register(
            'css_all',
            assets.Bundle(
                "bootstrap/dist/css/bootstrap.min.css",
                "fontawesome/css/font-awesome.css",
                assets.Bundle(
                    "main.sass",
                    filters='sass',
                    output="css_all.css"
                ),
                output="css_all.css"
            )
    )
    return env
