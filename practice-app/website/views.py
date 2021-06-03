from flask import Blueprint, render_template
from flask_login import login_required, current_user
import requests

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


def get_sport_names():
    uri = 'https://www.thesportsdb.com/api/v1/json/1/all_sports.php'

    r = requests.get(uri)
    
    result = r.json()

    sports={}

    for sport in result['sports']:
        sports[sport['idSport']] = sport['strSport']
    return sports



@views.route('create_event/')
@login_required
def create_event():
    sports = get_sport_names()
    return render_template("create_event.html", user= current_user, sports=sports)


