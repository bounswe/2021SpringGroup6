from flask import Blueprint, request
from ..models import Spectators
from .. import db
from flasgger.utils import swag_from
from sqlalchemy import exc

spectators = Blueprint('spectators', __name__)

# endpoint for declaring a person as interested to an event
# event is determined by the route, user should be passed as a paremeter
@spectators.route('/<event_id>/spectators', methods = ['POST'])
@swag_from('doc/spectators_post.yml', methods = ['POST'])
def declare_interest(event_id):
    if request.method == 'POST':
        # basic checks
        if not request.json:
            return {'error': 'Request is not in JSON format'}, 400
        if not 'user_id' in request.json:
            return {'error': "No user id provided"}, 400
        interested = Spectators(
            event_id = event_id,
            user_id = request.json['user_id'] #current_user
        )
    
    # insert into database
    try:
        db.session.add(interested)
        db.session.commit()
    except exc.NoReferenceError as e:
        db.session.rollback()
        return "Bad request", 400
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        return "Server problem", 503
    
    return interested.serialize(), 201