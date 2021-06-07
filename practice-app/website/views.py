from flask import Blueprint, render_template, jsonify, request, flash, redirect, url_for
from flask_login import login_required, current_user
import requests
import json

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('create_equipment/', methods=['POST','GET'])
@login_required
def create_equipment():
    if request.method == 'POST':
        equipment = {
            "name" : request.form.get("name")
        }

        # initialize request url and headers
        req = "http://127.0.0.1:5000/api/v1.0/equipments/"
        headers = {'Content-type': 'application/json'}
        
        # returns response of the request from the api
        response = requests.post(req, data=json.dumps(equipment), headers=headers)

        # handling the errors.
        # defining appropriate error codes.
        if response.status_code == 201:
            flash('Equipment Created', category='success')
            return redirect(url_for('views.home'))
        elif response.status_code == 400 :
            flash('Check Information Entered', category='error')
        elif response.status_code == 409 :
            flash('Equipment Already Exists!', category='error')
        else:
            flash('Error Occured, Try Again Later', category='error')
    
    return render_template("equipments.html", user=current_user)


@views.route('badge/', methods=['POST','GET'])
def badge():
    if request.method == "POST":
        badge = {
            "name" : request.form.get("name"),
            "symbol": request.form.get("symbol")
        }

        req = "http://localhost:5000/api/v1.0/badges"
        headers = {'Content-type': 'application/json'}
        response = requests.post(req, data=json.dumps(badge), headers=headers)
        result = response.content

        if response.status_code == 201:
            flash('Badge Added', category='success')
        else:
            flash('Error Occured, Try Again Later', category='error')

        return render_template("home.html", user= current_user)
    
    return render_template("badge.html", user= current_user)

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

        req = "http://127.0.0.1:5000/api/v1.0/events/"
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

@views.route('events/', methods=['POST', 'GET'])
@login_required
def event_search():
    # gets sport names and ids
    sports = get_sport_names()

    # initialize request url
    req = "http://127.0.0.1:5000/api/v1.0/events"

    # handle post request from frontend. in form input format
    if request.method == 'POST':

        # collect parameters
        params = []
        if request.form.get('name'):
            params.append("name=" + request.form.get('name'))
        if request.form.get('sport'):
             params.append("sport=" + request.form.get('sport'))
        if request.form.get('date_from'):
             params.append("date_from=" + request.form.get('date_from'))
        if request.form.get('date_to'):
             params.append("date_to=" + request.form.get('date_to'))

        # handle collected parameters. change url accordingly
        if params:
            req += "?"
            for par in params:
                req += (par + "&")
            req = req[:-1]
    
    # call api from event.py file
    headers = {'Content-type': 'application/json'}
    response = requests.get(req, headers = headers)

    # return rendered page
    if response.status_code == 200:
        flash('Events are fetched successfully', category='success')
        # TODO: When event page implemented, redirect to it.
        return render_template("event_search.html", user= current_user, sports=sports, events=response.json())
    elif response.status_code == 400 :
        flash('Check Information Entered', category='error')
    else:
        flash('Error Occured, Try Again Later', category='error')

  
@views.route('event/<event_id>', methods=['GET'])
def view_event(event_id):
    if request.method == 'GET':
        
        uri = f"http://127.0.0.1:5000/api/v1.0/events/{event_id}/"        
        res = requests.get(uri)      
        event = res.json()       
        icon = event["weather_icon"]
        weather_icon_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"
        return render_template("event_page_by_id.html", user = current_user, event = event, weather_icon_url = weather_icon_url)


