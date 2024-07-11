from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    from . import v1
    app.register_blueprint(v1.bp)

    return app
