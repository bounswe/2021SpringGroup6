from flask import Flask
from os import path


def create_app():
    app = Flask(__name__)
    #app.config['SECRET_KEY'] = <key>

    from .views import views
    from .api.event import events

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(events, url_prefix='/api/v1.0/events/')
    
    return app


