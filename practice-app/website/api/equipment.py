from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from ..models import Equipment
from .. import db
import requests
import json
from sqlalchemy import exc
from flasgger.utils import swag_from

equipments = Blueprint('equipments', __name__)

# returns the arbitrary price for equipment using an API
def get_price():
    url = 'https://api.blockchain.com/v3/exchange/tickers'
    response = requests.get(url)
    return response.json()[0]['price_24h']

# endpoint of the api of equipments
# applies a Post operation
# documentation for Post in .yml file
@equipments.route('/', methods=['POST'])
@swag_from('doc/equipments_POST.yml', methods=['POST'])
def post_equipment():
    # checking parameters
    if not request.json or not 'name' in request.json:
        return "Parameter not correct", 400

    result = request.json
    equipment_name = result['name']
    price = get_price()

    tempEquipment = Equipment.query.filter_by(name=equipment_name).first()
    
    # if equipment exists, returns code 409
    # handling error if an error occurs on Sqlalchemy
    # returns 201 if everything is fine
    if tempEquipment:
        return 'Equipment already exists!', 409
    else:
        new_equipment = Equipment(name=equipment_name, price=price)
        try:
            db.session.add(new_equipment)
            db.session.commit()
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            return "Try Later", 403

        return jsonify(new_equipment.serialize()), 201
