from flask import Blueprint, request,  url_for, jsonify, make_response, abort, flash
from ..models import Event
from .. import db
import requests

events = Blueprint('events', __name__)

API_KEY = '<api key>'


def getCoordinates(address):
    parameters = {'key': API_KEY , 'address': address}
    uri = 'https://maps.googleapis.com/maps/api/geocode/json'

    r = requests.get(uri, params=parameters)
    
    result = r.json()
    print(result)

    if r.status_code == 200:
        if result['status'] == "OK":
            formatted_address = result['results'][0]['formatted_address']
            longitude = result['results'][0]['geometry']['location']['lng']
            latitude = result['results'][0]['geometry']['location']['lat']
            return formatted_address, longitude, latitude, "OK"
        
    if result['status'] == "ZERO_RESULTS" or result['status'] == "INVALID_REQUEST": 
        return "",0,0,"Address Not Valid"
    elif result['status'] == "OVER_DAILY_LIMIT" or result['status'] == "OVER_QUERY_LIMIT" or result['status'] == "REQUEST_DENIED" or result['status'] == "UNKNOWN_ERROR": 
        return "",0,0,"Try Later"
    else:
        return "",0,0,"Try Later"

    


@events.route('/', methods = ['GET','POST'])
def event():
    if request.method == 'GET':
        eventList = Event.query.all()
        return jsonify([event_item.serialize() for event_item in eventList]), 201

    if request.method == 'POST':
        if not request.json or not 'name' in request.json or not 'creator_user'  in request.json or not 'location' in request.json:
            abort(400, description="Parameters not correct")
        
        formatted_address, longitude, latitude, error = getCoordinates(request.json['location'])

        if error != "OK":
            if error != "Try Later":
                abort(400, description = error)
            else:
                # TODO: If api not responding or full quota add without address fields
                abort(503, description = "Try Later" )

        new_event = Event(
            name = request.json['name'],
            date = request.json['date'] if 'date' in request.json else None,
            formatted_address = formatted_address,
            entered_address = request.json['location'],
            longitude = longitude,
            latitude = latitude,
            creator_user = request.json['creator_user']
        )

        db.session.add(new_event)
        db.session.commit()
        # TODO check database errors - foreign key error
        
        return jsonify(new_event.serialize()), 201
