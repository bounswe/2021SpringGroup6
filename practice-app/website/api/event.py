from flask import Blueprint, request,  url_for, jsonify, make_response, abort

events = Blueprint('events', __name__)

@events.route('events/', methods = ['POST'])
def create_event():
    return jsonify({'event': {"name": "Temp"}}), 201
