from flask import Blueprint, request,  url_for, jsonify, make_response, abort, flash
from ..models import Event, User
from .. import db
import requests
from flasgger.utils import swag_from
from sqlalchemy import exc
events = Blueprint('events', __name__)
import re

API_KEY = '<api key>'

"""
    Get coordinates using Google Maps API

    parameters:
        address: "address of the location" 
    return:
        True if valid False otherwise
"""
def getCoordinates(address):

    # Make GET request to the uri using API_KEY
    parameters = {'key': API_KEY , 'address': address}
    uri = 'https://maps.googleapis.com/maps/api/geocode/json'

    r = requests.get(uri, params=parameters)
    
    result = r.json()

    # If there is no error return information from response.
    if r.status_code == 200:
        if result['status'] == "OK":
            formatted_address = result['results'][0]['formatted_address']
            longitude = result['results'][0]['geometry']['location']['lng']
            latitude = result['results'][0]['geometry']['location']['lat']
            return formatted_address, longitude, latitude, "OK"
    
    # Address not valid, error messages from API docs
    if result['status'] == "ZERO_RESULTS" or result['status'] == "INVALID_REQUEST": 
        return "",0,0,"Address Not Valid"
    # Cannot make a request
    elif result['status'] == "OVER_DAILY_LIMIT" or result['status'] == "OVER_QUERY_LIMIT" or result['status'] == "REQUEST_DENIED" or result['status'] == "UNKNOWN_ERROR": 
        return "",0,0,"Try Later"
    # Remaining Errors
    else:
        return "",0,0,"Try Later"


"""
    Check the validity of the sport field of event

    parameters:
        new_event: Event 
    return:
        True if valid False otherwise
"""
def check_event_sport(new_event):
    # sport Ids between 102-120
    if int(new_event.sport) < 102 or int(new_event.sport) > 120:
        return False
    return True

"""
    Check the format of the date field of event
    Format should match YYYY-MM-DDTHH:MM

    parameters:
        new_event: Event 
    return:
        True if valid False otherwise
"""
def check_event_date(new_event):
    # Date format YYYY-MM-DDTHH:MM
    date_regex = "^(20[0-9][0-9])-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])T(0[1-9]|1[0-9]|2[0-3]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]2|5[0-9])$"
    if not re.match(date_regex, new_event.date):
        return False
    return True


@events.route('/', methods = ['GET','POST'])
@swag_from('doc/events_POST.yml', methods=['POST'])
def event():
    if request.method == 'GET':
        eventList = Event.query.all()
        return jsonify([event_item.serialize() for event_item in eventList]), 201

    if request.method == 'POST':
        """
            Used to create a new event.
            Endpoint description:
                ./api/v.10/events
                'POST':
                    JSON Request Body Format : {
                                                name = "Name of the event, title." required,
                                                creator_user = "Id of the user creating the event. Id must be registered to a user." required,
                                                location = "Address of the event, given using basic English." required,
                                                sport = "Id of the sport. Between 102-120." required,
                                                date ="Date of the event. Format is "YYYY-MM-DDTHH:MM" required
                                            }
                    Response Example : {
                                            "creator_user": 1,
                                            "date": "10.12.2021",
                                            "entered_address": "Trabzon",
                                            "formatted_address": "Trabzon, Ortahisar/Trabzon, Turkey",
                                            "id": 2,
                                            "latitude": 41.0026969,
                                            "longitude": 39.7167633,
                                            "name": "abc",
                                            "sport": 103
                                        }
                    Status Codes:
                        201: "Event created and added to database."
                        400: "Body parameters are not correct."
                        403:  "There is an error, try later."


        """

        # All parameters must be present.
        if not request.json or not 'name' in request.json or not 'creator_user'  in request.json or not 'location' in request.json or not 'sport' in request.json or not 'date' in request.json:
            return jsonify({"error":"Parameters not correct"}), 400

        # Get coordinates using Google Maps API.
        formatted_address, longitude, latitude, error = getCoordinates(request.json['location'])

        # Return error if fetch was not correct.
        if error != "OK":
            if error != "Try Later":
                return jsonify({"error": error}), 400
            else:
                return jsonify({"error": "Try Later"}), 403

        # Create database model
        new_event = Event(
            name = request.json['name'],
            date = request.json['date'],
            formatted_address = formatted_address,
            entered_address = request.json['location'],
            longitude = longitude,
            latitude = latitude,
            creator_user = request.json['creator_user'],
            sport = request.json['sport']
        )

        # Check if creator_user is valid and there is a user registered with that id.
        user = User.query.get(request.json['creator_user'])
        if not user:
            return "User Not Registered 5", 400

        # Check sport id.
        if not check_event_sport(new_event):
            return jsonify({"error":"Sport Id Is Not Correct"}), 400

        # Check date format.
        if not check_event_date(new_event):
            return jsonify({"error":"Date Format Not Correct"}), 400


        try:
            # Add Event to database.
            db.session.add(new_event)
            db.session.commit()
        except exc.SQLAlchemyError as e:
            # In case of error, return error message
            db.session.rollback()
            return jsonify({"error": "Try Later"}), 403
        
        # No error, return new event information
        return jsonify(new_event.serialize()), 201
