from flask import Blueprint, render_template, request, flash, json, redirect, url_for
from flask_login import login_required, current_user
from .models import Equipment
from . import db
import requests
import json

equipment = Blueprint('equipment', __name__)

@equipment.route('/', methods=['GET', 'POST'])
@login_required
def post_equipment():
    if request.method == 'POST':

        req = requests.get('https://api.blockchain.com/v3/exchange/tickers')
        data = json.loads(req.content)

        price = data[0]['price_24h']

        enteredEquipment = request.form.get('equipment')

        tempEquipment = Equipment.query.filter_by(equipmentName=enteredEquipment).first()
        if tempEquipment:
            flash('Equipment already exists!.', category='error')
        else:
            new_equipment = Equipment(equipmentName=enteredEquipment, price=price)
            db.session.add(new_equipment)
            db.session.commit()
            flash('Successfull', category='success')


    return render_template("equipments.html", user=current_user)