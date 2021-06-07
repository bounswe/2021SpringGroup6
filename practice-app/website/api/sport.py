from flask import Blueprint, request,  url_for, jsonify, make_response, abort, flash
from ..models import Sport
from .. import db
from flasgger.utils import swag_from
from sqlalchemy import exc

sports = Blueprint('sports', __name__)

def get_sport_by_keyword(sports, keyword):
    result = []
    for sport in sports:
        if keyword in sport.sport:
            result.append(sport)
    
    return result

"""
    Used to get sports filtered by a keyword.
    Endpoint description:
        ./api/v.10/sports?keyword=sp
        'GET':
            Response Example : {
                                    "sports": [
                                        {
                                            "id": 103,
                                            "sport": "Motorsport"
                                        }
                                    ]
                                }
            Status Codes:
                200: "Result returned with no error"
                503: "Service unavailable"

"""
@sports.route('/', methods = ['GET'])
@swag_from('doc/sport_GET.yml', methods=['GET'])
def sport():
    try:
        # Get all sports.
        sports = Sport.query.all()

        # Get keyword parameter.
        keyword = request.args.get('keyword') if 'keyword' in request.args else ""

        # Filter by keyword.
        result = get_sport_by_keyword(sports, keyword)

        # Return filtered result. 
        return jsonify({"sports":[s.serialize() for s in result]}), 200
    except:
        # Some error occured.
        return jsonify({"error":"Service unavailable"}), 403