from flask import Blueprint, render_template, jsonify, request, flash, redirect, url_for
from flask_login import login_required, current_user
import requests
import json

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



@views.route('/events/<event_id>/discussions', methods=["GET"])
@login_required
def discussionPage(event_id):
    
    BASE = 'http://127.0.0.1:5000/'  #  should be changed
    response = requests.get(BASE + '/api/v1.0/events/' + event_id + '/discussions')
    description = response.json()["description"]
    text = response.json()["text"]
    return render_template("discussionPage.html", event_id=event_id, definition = description, text = text.split('#')) 


@views.route('/events/<event_id>/discussionPost', methods=["GET", "POST"])
@login_required
def discussionPost(event_id):
    
    if request.method == 'GET':
        return render_template("discussionPost.html", event_id=event_id)
    else:
        message = {"text" : request.form.get('comment')}

        BASE = 'http://127.0.0.1:5000/'  #  should be changed
        
        headers = {'Content-type': 'application/json'}
        response = requests.post(BASE + '/api/v1.0/events/' + event_id + '/discussions', data=json.dumps(message), headers=headers)
       
        if response.status_code == 201:
            flash('Comment Posted', category='success')
            return redirect(url_for('views.discussionPage', event_id=event_id))
        elif response.status_code == 400 :
            flash('Text cannot be empty', category='error')
        else:
            flash('Error Occured, Try Again Later', category='error')

        return redirect(url_for('views.discussionPost', event_id=event_id))

        

    


