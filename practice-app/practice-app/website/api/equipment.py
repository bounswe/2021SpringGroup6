from flask import Blueprint, render_template, request, flash, json, redirect, url_for
from flask_login import login_required, current_user
from ..models import Equipment
from .. import db
import requests
import json

equipments = Blueprint('equipments', __name__)

@equipments.route('/', methods=['GET', 'POST'])
@login_required
def post_equipment():
    if request.method == 'POST':

        if not request.json or not 'name' in request.json:
            return "Parameter not correct", 400

        req = requests.get('https://api.blockchain.com/v3/exchange/tickers')
        result = req.json()

        print(result)

        data = json.loads(req.content)

        price = data[0]['price_24h']

        enteredEquipment = request.form.get('equipment')

        tempEquipment = Equipment.query.filter_by(equipmentName=enteredEquipment).first()
        if tempEquipment:
            flash('Equipment already exists!.', category='error')
        else:
            new_equipment = Equipment(equipmentName=enteredEquipment, price=price)
            
            try:
                db.session.add(new_equipment)
                db.session.commit()
                flash('Successfull', category='success')
            except exc.NoReferenceError as e:
                db.session.rollback()
                return "User Not Registered", 400
            except exc.SQLAlchemyError as e:
                db.session.rollback()
                return "Try Later", 403



    return jsonify(new_equipment.serialize()), 201