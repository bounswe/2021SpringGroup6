from flask import Blueprint, request, render_template, flash,jsonify
import requests
from ..models import Badge
from .. import db
from sqlalchemy import exc
from flasgger.utils import swag_from

badges = Blueprint('badges',__name__)

def get_badge_point():
    url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
    headers = {'X-CoinAPI-Key' : '206D8179-A9A3-4C59-860B-84C1E511EB55'}
    response = requests.get(url, headers=headers)

    return str(response.json()['rate']).split('.')[1][3]

@badges.route('/',methods = ['POST'])
@swag_from('doc/badges_POST.yml', methods=['POST'])
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
        db.session.rollback()
        return "Try Later", 403
        
    return jsonify(badge.serialize()), 201

@badges.route('show_badge/',methods = ['GET','POST'])
def show_badge():
    if request.method == 'POST':
        badges = Badge.query.all()
        badges_serialized = []
        for badge in badges:
            badges_serialized.append(badge.serialize())
        url = 'https://thatcopy.pw/catapi/rest/'
        dog_photos = [requests.get(url).json()['url'] for _ in badges] 
        control = True
        result = {"badges":badges_serialized, "dog_photos":dog_photos, "control":control}
        #return render_template("index.html", badges=zip(badges,dog_photos), control=control)
        return jsonify(result), 201
        
    else:
        badges = Badge.query.all()
        control = False
        result = {"control":control}
        #return render_template("index.html", control=control)
        return jsonify(result),201
