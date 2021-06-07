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


@sports.route('/', methods = ['GET'])
@swag_from('doc/events_POST.yml', methods=['GET'])
def sport():
    sports = Sport.query.all()
    keyword = request.args.get('keyword') if 'keyword' in request.args else ""

    result = get_sport_by_keyword(sports, keyword)

    return jsonify({"sports":[s.serialize() for s in result]}), 200