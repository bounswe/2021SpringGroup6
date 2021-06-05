from flask import Blueprint, render_template, jsonify, request, flash, redirect, url_for
from flask_login import login_required, current_user
import requests
import json

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('create_equipment/', methods=['POST','GET'])
@login_required
def create_equipment():
    if request.method == 'POST':
        equipment = {
            "name" : request.form.get('equipment')
        }

        req = "http://127.0.0.1:5000/api/v1.0/equipments"
        headers = {'Content-type': 'application/json'}
        response = requests.post(req, data=json.dumps(equipment), headers=headers)
        result = response.content

        # print(response.status_code, "************") Error Code: 500

        if response.status_code == 201:
            flash('Equipment Created', category='success')
            return redirect(url_for('views.home'))
        elif response.status_code == 400 :
            flash('Check Information Entered', category='error')
        else:
            flash('Error Occured, Try Again Later', category='error')
    
    return render_template("equipments.html", user= current_user)