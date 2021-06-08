from flask import Blueprint, request, render_template, flash,jsonify
import requests
from ..models import Badge
from .. import db
from sqlalchemy import exc
from flasgger.utils import swag_from

badges = Blueprint('badges',__name__)

def extract_point(price):
    return str(price).split('.')[1][3]

def get_badge_point():
    """
    This is a function to assign a point to the badge.
    It uses a Bitcoin Price API and get a number from that price.
    """
    url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
    headers = {'X-CoinAPI-Key' : '206D8179-A9A3-4C59-860B-84C1E511EB55'}
    response = requests.get(url, headers=headers)

    return extract_point(response.json()['rate'])

def prepare_badge(data):
    badge_name = data['name']
    badge_symbol = data['symbol']
    badge = Badge(name=badge_name, symbol=badge_symbol)

    return badge

@badges.route('/',methods = ['POST'])
@swag_from('doc/badges_POST.yml')
def add_badge():
    """
    This is an only POST endpoint for adding a badge.
    In order to add a badge "name" and "symbol" which is a URL for a symbol are needed.
    If the badge is added successfully, it returns 201 response code.
    If there is a problem during the addition of the badge, it returns 403 response code.
    """

    badge = prepare_badge(request.json)
    badge.badge_point = get_badge_point()
    try:
        db.session.add(badge)
        db.session.commit()
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        return "Try Later", 403
        
    return jsonify(badge.serialize()), 201