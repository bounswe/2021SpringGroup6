from flask import Blueprint, request
from ..models import Spectators
from .. import db
from flasgger.utils import swag_from
from sqlalchemy import exc

spectators = Blueprint('spectators', __name__)


@spectators.route('/<event_id>/spectators', methods = ['POST'])
@swag_from('doc/spectators_post.yml', methods = ['POST'])
def declare_interest(event_id):
    """
    Endpoint for declaring a person as spectator to an event
    Event is determined by the route, user should be passed as a paremeter
    
    """
    if request.method == 'POST':
        # basic checks
        if not request.json:
            return {'error': 'Request is not in JSON format'}, 400
        if not 'user_id' in request.json:
            return {'error': "No user id provided"}, 400
        spectator = Spectators(
            event_id = event_id,
            user_id = request.json['user_id'] #current_user
        )
    
    # insert into database
    try:
        db.session.add(spectator)
        db.session.commit()
    except exc.NoReferenceError as e:
        db.session.rollback()
        return "Bad request", 400
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        return "Server problem", 503
    
    return spectator.serialize(), 201