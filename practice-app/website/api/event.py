from flask import Blueprint, json, request,  url_for, jsonify, make_response, abort, flash
from ..models import Event
from .. import db
import requests
from ..views import get_sport_names
from flasgger.utils import swag_from
from sqlalchemy import exc
events = Blueprint('events', __name__)


API_KEY = '<api_key_coordinates>'
API_KEY2 = '<api_key_weather>'

def get_weather(latitude, longitude):
    parameters = {'lat': latitude, 'lon' : longitude, 'appid': API_KEY2 }
    uri = 'https://api.openweathermap.org/data/2.5/weather'
    r = requests.get(uri, params=parameters)
    r = r.json()
    return r["weather"][0]["description"], r["weather"][0]["icon"]


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

    
#helper method for querying
def query_handler_events(name, sport, date_from, date_to):
    query = 'SELECT * FROM Event WHERE'
    filters = []
    # adds filter for name
    if name:
        filters.append(' name LIKE \'%' + name + '%\' AND')
    # adds filter for sport name
    if sport:
        filters.append(' sport = ' + str(sport) + ' AND')
    # adds filter for initial date
    if date_from:
        filters.append(' date >= \'' + date_from + '\' AND')
    # adds filter for final date
    if date_to:
        filters.append(' date <= \'' + date_to + '\' AND')

    # checks if there is any filter added
    if filters:
        for filt in filters:
            query += filt
        query = query[:-4] + ';'
    else:
        query = query[:-6] + ';'

    return query

@events.route('/', methods = ['GET','POST'])
@swag_from('doc/events_POST.yml', methods=['POST'])
@swag_from('doc/events_GET.yml', methods=['GET'])
def event():
    # handles get request
    if request.method == 'GET':
        # fethes body parameters
        query_parameters = request.args
        name = query_parameters.get('name')
        sport = query_parameters.get('sport')
        date_from = query_parameters.get('date_from')
        date_to = query_parameters.get('date_to')

        print(query_parameters.get('date_from'))
        # sets up querys
        query = query_handler_events(name, sport, date_from, date_to)
        print(query)

        # executes query and converts to json format
        eventList = db.engine.execute(query)
        eventList = json.dumps([dict(event_item) for event_item in eventList])

        # temporary parameter for adding additional info into result
        temp = json.loads(eventList)

        # external api for assigning random names for event creators
        multi = requests.get('https://randomuser.me/api/?inc=name&results=' + str(len(temp))).json()['results']
        
        # adds external info into the result
        for index, item in enumerate(temp):
            name = multi[index]['name']
            item['creator_name'] = name['first'] + ' ' + name['last']
        
        # returns the result in json format
        return jsonify(temp)
        

    if request.method == 'POST':
        if not request.json or not 'name' in request.json or not 'creator_user'  in request.json or not 'location' in request.json or not 'sport' in request.json or not 'date' in request.json:
            return "Parameters not correct", 400
        
        formatted_address, longitude, latitude, error = getCoordinates(request.json['location'])

        if error != "OK":
            if error != "Try Later":
                return error, 400
            else:
                # TODO: If api not responding or full quota add without address fields
                return "Try Later", 403

        new_event = Event(
            name = request.json['name'],
            date = request.json['date'] if 'date' in request.json else None,
            formatted_address = formatted_address,
            entered_address = request.json['location'],
            longitude = longitude,
            latitude = latitude,
            creator_user = request.json['creator_user'],
            sport = request.json['sport']
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


@events.route('/<event_id>/', methods = ['GET'])
@swag_from('doc/event_GET.yml', methods=['GET'])
def get_event_by_id(event_id):
    if request.method == 'GET':
        event = Event.query.get(event_id)      
        event_with_weather = event.serialize()
        event_with_weather["hour"] =  event_with_weather["date"][11:]
        event_with_weather["date"] = event_with_weather["date"][:10]     
        weather, weather_icon = get_weather(event_with_weather["latitude"], event_with_weather["longitude"])
        event_with_weather["weather"] = weather
        event_with_weather["weather_icon"] = weather_icon
        sport_names = get_sport_names()       
        event_with_weather["sport"] = sport_names[str(event_with_weather["sport"])]                
        return jsonify(event_with_weather), 200
