from flask import Blueprint, render_template,request,flash
from flask_login import login_required, current_user
import requests, json

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('badge/', methods=['POST','GET'])
def badge():
    if request.method == "POST":
        badge = {
            "name" : request.form.get("name"),
            "symbol": request.form.get("symbol")
        }

        req = "http://localhost:5000/api/v1.0/badges"
        headers = {'Content-type': 'application/json'}
        response = requests.post(req, data=json.dumps(badge), headers=headers)
        result = response.content

        if response.status_code == 201:
            flash('Badge Added', category='success')
        else:
            flash('Error Occured, Try Again Later', category='error')

        return render_template("home.html", user= current_user)
    
    return render_template("badge.html", user= current_user)


