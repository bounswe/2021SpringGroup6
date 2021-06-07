from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flasgger import Swagger

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'cmpe'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    swagger = Swagger(app)

    db.init_app(app)

    
    from .views import views
    from .api.auth import auth
    from .api.event import events
    from .api.badge import badges
    from .api.equipment import equipments

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(events, url_prefix='/api/v1.0/events/')
    app.register_blueprint(badges, url_prefix='/api/v1.0/badges/')
    app.register_blueprint(equipments, url_prefix='/api/v1.0/equipments/')
    
    from .models import User, Event

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('../website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
