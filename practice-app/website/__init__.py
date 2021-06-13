from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flasgger import Swagger
import requests


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'cmpe'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database/{DB_NAME}'

    swagger = Swagger(app)

    db.init_app(app)

    
    from .views import views
    from .api.auth import auth
    from .api.event import events
    from .api.badge import badges
    from .api.interesteds import interesteds
    from .api.spectators import spectators
    from .api.sport import sports
    from .api.equipment import equipments

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(events, url_prefix='/api/v1.0/events/')
    app.register_blueprint(badges, url_prefix='/api/v1.0/badges/')
    app.register_blueprint(interesteds, url_prefix='/api/v1.0/events/')
    app.register_blueprint(equipments, url_prefix='/api/v1.0/equipments/')
    app.register_blueprint(spectators, url_prefix='/api/v1.0/events/')
    app.register_blueprint(sports, url_prefix='/api/v1.0/sports/')

    
    from .models import User, Event, Equipment

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def get_sport_names():
    uri = 'https://www.thesportsdb.com/api/v1/json/1/all_sports.php'

    r = requests.get(uri)
    
    result = r.json()

    sports={}

    for sport in result['sports']:
        sports[sport['idSport']] = sport['strSport']
    return sports

"""
    If database does not exist, create a database. Also sport table is filled
"""
def create_database(app):
    if not path.exists('website/database/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
        # Get sports
        sports = get_sport_names()
        from .models import Sport
        # Add sports to database
        with app.app_context():
            for sport in sports.keys():
                new_sport = Sport(
                    id = sport,
                    sport =  sports[sport]
                )
                try:
                    db.session.add(new_sport)
                    db.session.commit()
                except:
                    #Already exists
                    pass

