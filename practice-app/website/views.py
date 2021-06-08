from flask import Blueprint, render_template, jsonify, request, flash, redirect, url_for
from flask_login import login_required, current_user
import requests
import json

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('badge/', methods=['POST','GET'])
def badge():
    """
    This prepares the front-end side of the badge addition functionality.
    It can be used as a POST and GET. When it is used as a GET, badge addition page is shown to provide related fields for it.
    When it is used as a POST, the provided fields for a badge is posted and badge post endpoint is requested.
    """
    if request.method == "POST":
        badge = {
            "name" : request.form.get("name"),
            "symbol": request.form.get("symbol")
        }

        req = "http://localhost:5000/api/v1.0/badges"
        headers = {'Content-type': 'application/json'}
        response = requests.post(req, data=json.dumps(badge), headers=headers)

        if response.status_code == 201:
            flash('Badge Added', category='success')
        else:
            flash('Error Occured, Try Again Later', category='error')

        return render_template("home.html", user= current_user)
    
    return render_template("badge.html", user= current_user)

@views.route('point_badge/', methods=['POST','GET'])
def point_badge():
    """
    This prepares the front-end side of the badge point retrieval.
    It can be used as a POST and GET. When it is used as a GET, badge point retrieval page is shown.
    When it is used as a POST, badge point for a given badge name is shown.
    """
    if request.method == "POST":

        badge_name = request.form.get('name')
        req = f'http://127.0.0.1:5000/api/v1.0/badges/point?name={badge_name}'
        headers = {'Content-type': 'application/json'}
        response = requests.get(req, headers=headers)

        if response.status_code != 200:
            flash(response.text, category='error')
            return render_template("home.html", user=current_user)
            
        return render_template("show_badge_point.html", user=current_user, badge=response.json())
    
    return render_template("point_badge.html", user=current_user)

def get_sport_names():
    uri = 'https://www.thesportsdb.com/api/v1/json/1/all_sports.php'

    r = requests.get(uri)
    
    result = r.json()

    sports={}

    for sport in result['sports']:
        sports[sport['idSport']] = sport['strSport']
    return sports


@views.route('create_event/', methods=['POST','GET'])
@login_required
def create_event():
    sports = get_sport_names()
    if request.method == 'POST':
        event = {
            "name" : request.form.get('name'),
            "date" : request.form.get('date'),
            "location" : request.form.get('location'),
            "sport" : request.form.get('sport'),
            "creator_user" : current_user.id
        }

        req = "http://127.0.0.1:5000/api/v1.0/events"
        headers = {'Content-type': 'application/json'}
        response = requests.post(req, data=json.dumps(event), headers=headers)
        result = response.content

        if response.status_code == 201:
            flash('Event Created', category='success')
            # TODO: When event page implemented, redirect to it.
            return redirect(url_for('views.home'))
        elif response.status_code == 400 :
            flash('Check Information Entered', category='error')
        else:
            flash('Error Occured, Try Again Later', category='error')
    
    return render_template("create_event.html", user= current_user, sports=sports)

