from flask import Blueprint, request,  url_for, jsonify, make_response, abort
from flasgger.utils import swag_from

events = Blueprint('events', __name__)

@events.route('events/', methods = ['POST'])
@swag_from('doc/events_POST.yml', methods=['POST'])
def create_event():
    return jsonify({'event': {"name": "Temp"}}), 201
