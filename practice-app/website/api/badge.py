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


def get_cat_pictures(badges):
    """This is the function that returns a picture for all
    elements in the parameter list."""

    url = 'https://thatcopy.pw/catapi/rest/'
    
    return [requests.get(url).json()['url'] for _ in badges] 
        

@badges.route('show_badge/',methods = ['GET','POST'])
@swag_from('doc/badges_GET.yml', methods=['POST'])
def show_badge():
    """
    This function is the that shows all the badges after the user
    clicks the button. It uses RandomCat API to show random cat pictures.
    Since it starts working with a POST request from the server, first 
    thing it does is checking request method. 
    Then it gets all the badges from the database and return a json that contains cat photos.

    control variable provides that if the button is not clicked yet, it returns False and 
    there will be no table. If the button is clicked control is True and there will be a 
    table on the html file.
    """
    if request.method == 'GET':
        badges = Badge.query.all()
        badges_serialized = [i.serialize() for i in badges]
        
        cat_photos = get_cat_pictures(badges)

        control = True
        result = {"badges":badges_serialized, "dog_photos":cat_photos, "control":control}
        return jsonify(result), 200
        
    else:
        control = False
        result = {"control":control}
        return jsonify(result),200
