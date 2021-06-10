from flask import Blueprint, request, jsonify
from ..models import Spectators
from .. import db
from flasgger.utils import swag_from
from sqlalchemy import exc

spectators = Blueprint('spectators', __name__)

@spectators.route('/<event_id>/spectators', methods = ['POST'])
@swag_from('doc/spectators_post.yml', methods = ['POST'])
def add_as_spectator_to_event(event_id):
    
    """
    Endpoint for adding a user as a spectator to an event.
    event_id is a path parameter and the user_id should be in the request body.
    Endpoint description:
        ./api/v1.0/events/<event_id>/spectators
        'GET':
            JSON Request Body Format :      {
                                                "user_id" = id of the user who will be added as spectator to the event, required.                             
                                            }
            Response Example : {
                                    "event_id": 45,
                                    "user_id": 1764
                                }
            Status Codes:
                201: "The user has been added to the event as spectator"
                400: "Bad request"
                503: "Server problem"
    """
    if request.method == 'POST':  
        # check if the request body is in json format  
        if not request.json:
            return jsonify({'error': 'request body is not in JSON format'}), 400
        if not 'user_id' in request.json:
            return {'error': "user id is not given"}, 400
        # create the spectator which will be inserted into the database
        spectator = Spectators(
            event_id = event_id,
            user_id = request.json['user_id'] 
        )
    
        # insert into the database
        try:
            db.session.add(spectator)
            db.session.commit()
        except exc.NoReferenceError as e:
            db.session.rollback()
            return "Bad request", 400
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            return "Server problem", 503
        
        return jsonify(spectator.serialize()), 201