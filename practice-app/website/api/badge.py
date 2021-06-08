from flask import Blueprint, request, jsonify
import requests
from ..models import Badge
from .. import db
from sqlalchemy import exc
from flasgger.utils import swag_from
from sqlalchemy import select

badges = Blueprint('badges',__name__)

def extract_point(price):
    return str(price).split('.')[1][3]

def create_badge_point():
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
@swag_from('doc/badges_POST.yml', methods = ['POST'])
def add_badge():
    """
    This is an only POST endpoint for adding a badge.
    In order to add a badge "name" and "symbol" which is a URL for a symbol are needed.
    If the badge is added successfully, it returns 201 response code.
    If there is a problem during the addition of the badge, it returns 503 response code.
    """

    badge = prepare_badge(request.json)
    badge.point = create_badge_point()
    try:
        db.session.add(badge)
        db.session.commit()
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        return "Try Later", 503
        
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

@badges.route('/point/',methods = ['GET'])
@swag_from('doc/badges_point_get.yml', methods = ['GET'])
def get_badge_point():
    """
    This is an only GET endpoint for getting the point of a badge by name.
    Badge name should be provided.
    If the badge point is fetched successfully, it returns 201 response code
    If there is no badge with the given name it returns 400 response code.
    If there is a problem during the fetch, it returns 503 response code.
    """
    badge_name = request.args.get('name')
    try:
        badge = db.session.query(Badge.point).filter(Badge.name==badge_name).first()
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        return "Error Occured, Try Again Later", 503
    
    if badge is None:
        return "No badge with this Name", 400   
    return {'name': badge_name, 'point':badge[0]}, 200

