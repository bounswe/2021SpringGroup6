from flask import Blueprint, request, render_template, flash
import requests
from ..models import Badge
from .. import db

badges = Blueprint('badges',__name__)

def get_badge_point():
    url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
    headers = {'X-CoinAPI-Key' : '206D8179-A9A3-4C59-860B-84C1E511EB55'}
    response = requests.get(url, headers=headers)

    return str(response.json()['rate']).split('.')[1][3]

@badges.route('/',methods = ['POST'])
def add_badge():
    result = request.form
    badge_name = result['Name']
    badge_point = get_badge_point()
    badge_symbol = result['URL']
    badge = Badge(name=badge_name, symbol=badge_symbol, point=badge_point)
    db.session.add(badge)
    db.session.commit()
    flash('Badge is added successfully!.', category='success')
    return render_template('badge.html'), 201