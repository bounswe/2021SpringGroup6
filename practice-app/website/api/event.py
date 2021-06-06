from re import template
from flask import Blueprint, request,  url_for, jsonify, make_response, abort, flash
from sqlalchemy.sql.elements import Null
from ..models import Event, DiscussionPost, Sports
from .. import db
import json
import sqlite3
import requests
from flasgger.utils import swag_from
from sqlalchemy import exc
events = Blueprint('events', __name__)

API_KEY = 'AIzaSyB918Ru6ZsU1P3OPc-IaE_lRLgjNM1Suyk'


def getCoordinates(address):
    parameters = {'key': API_KEY, 'address': address}
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
        return "", 0, 0, "Address Not Valid"
    elif result['status'] == "OVER_DAILY_LIMIT" or result['status'] == "OVER_QUERY_LIMIT" or result['status'] == "REQUEST_DENIED" or result['status'] == "UNKNOWN_ERROR":
        return "", 0, 0, "Try Later"
    else:
        return "", 0, 0, "Try Later"


@events.route('/', methods=['GET', 'POST'])
@swag_from('doc/events_POST.yml', methods=['POST'])
def event():

    if request.method == 'GET':
        eventList = Event.query.all()
        return jsonify([event_item.serialize() for event_item in eventList]), 201

    if request.method == 'POST':
        if not request.json or not 'name' in request.json or not 'creator_user' in request.json or not 'location' in request.json or not 'sport' in request.json:
            return "Parameters not correct", 400

        formatted_address, longitude, latitude, error = getCoordinates(
            request.json['location'])

        if error != "OK":
            if error != "Try Later":
                return error, 400
            else:
                # TODO: If api not responding or full quota add without address fields
                return "Try Later", 403

        new_event = Event(
            name=request.json['name'],
            date=request.json['date'] if 'date' in request.json else None,
            formatted_address=formatted_address,
            entered_address=request.json['location'],
            longitude=longitude,
            latitude=latitude,
            creator_user=request.json['creator_user'],
            sport=request.json['sport']
        )

        try:
            db.session.add(new_event)
            db.session.commit()
        except exc.NoReferenceError as e:
            db.session.rollback()
            return "User Not Registered", 400
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            return "Try Later", 403

        return jsonify(new_event.serialize()), 201


# When the id of the event given, corresponding discussion is returned by adding the definition of the sport type in the json format
# Corresponding event must exist and have a sport type in db.
@events.route('<event_id>/discussions', methods=['GET', 'POST'])
@swag_from('doc/discussionForEvent_GET.yml', methods=['GET'])
@swag_from('doc/discussionForEvent_POST.yml', methods=['POST'])
def discussionForEvent(event_id):

    if request.method == 'GET':

        if int(event_id) <=-1:
            return "Wrong path parameters", 401
        try:
            eventList = Event.query.all()
        except exc.NoReferenceError as e:
            return "Database error", 400
        eventList = Event.query.all()


        sportName = ''

        # Finds the event with the given id and its sport type
        for i in range(len(eventList)):
            if eventList[i].serialize()["id"] == int(event_id):
                sportName = eventList[i].serialize()["sport"]


        # ############# New

        sportList = Sports.query.all()

        for i in range(len(sportList)):
            if sportList[i].serialize()["id"] == int(sportName):
                sportName = sportList[i].serialize()["sport"]

  
        ############# New

        description = 'No definition found for ' + sportName

        # Find the corresponding definition for the sport type
        response = requests.get(
            'https://sports.api.decathlon.com/sports/' + sportName.lower())  # API to use
        if response.status_code >= 200 and response.status_code < 300:
            json_data = json.loads(response.text)
            description = json_data['data']['attributes']['description']
            if description == None:
                description = 'No definition found for ' + sportName

        try:
            discussionPostList = DiscussionPost.query.all()
        except exc.NoReferenceError as e:
            return "Database error", 400

        discussionPostList = DiscussionPost.query.all()
        # Get the discussion from the database for the given event
        text = 'No discussion found'

        for i in range(len(discussionPostList)):
            if discussionPostList[i].serialize()["id"] == int(event_id):
                text = discussionPostList[i].serialize()["text"]

        result = {"id": event_id, "description": description, "text": text}
        return jsonify(result), 201
