from flask import Blueprint, request, render_template, flash,jsonify
import requests
from ..models import Badge
from .. import db
from sqlalchemy import exc

badges = Blueprint('badges',__name__)

def get_badge_point():
    url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
    headers = {'X-CoinAPI-Key' : '206D8179-A9A3-4C59-860B-84C1E511EB55'}
    response = requests.get(url, headers=headers)

    return str(response.json()['rate']).split('.')[1][3]

@badges.route('/',methods = ['POST'])
def add_badge():
    result = request.json
    badge_name = result['name']
    badge_point = get_badge_point()
    badge_symbol = result['symbol']
    badge = Badge(name=badge_name, symbol=badge_symbol, point=badge_point)
    try:
        db.session.add(badge)
        db.session.commit()
    except exc.SQLAlchemyError as e:
        return str(e.__dict__['orig']), 400
        
    return jsonify(badge.serialize()), 201