from flask import Flask
from flask import Blueprint

app = Flask(__name__)
auth = Blueprint('auth', __name__)

def create_app(config_name)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='')

    return app


from app import views
