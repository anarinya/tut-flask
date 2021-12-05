from flask import Flask


def create_app():
    """
    Create a Flask application using the app factory pattern.
    :return: Flask app
    """
    # instance_relative_config: look for an instance module in the main dir
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    # silent=True: fall back to config settings if instance settings don't exist
    app.config.from_pyfile('settings.py', silent=True)

    @app.route('/')
    def index():
        """
        Render a Hello World response.
        :return: Flask response
        """
        return app.config['HELLO']

    return app
