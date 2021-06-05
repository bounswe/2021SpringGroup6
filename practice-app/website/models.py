from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

class Badge(db.Model):
    badgeID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    symbol = db.Column(db.String(200))
    point = db.Column(db.Integer)

    def serialize(self):
        """Return object data in JSON serializable format"""
        return {
            'badgeID'                : self.badgeID,
            'name'                   : self.name,
            'symbol'                 : self.symbol,
            'point'                  : self.point
        }

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    date = db.Column(db.Text)
    formatted_address = db.Column(db.Text)
    entered_address = db.Column(db.Text)
    longitude = db.Column(db.Float())
    latitude = db.Column(db.Float())
    creator_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    sport = db.Column(db.Integer)

    def serialize(self):
       """Return object data in JSON serializable format"""
       return {
           'id'                     : self.id,
           'name'                   : self.name,
           'date'                   : self.date,
           'formatted_address'      : self.formatted_address,
           'entered_address'        : self.entered_address,
           'longitude'              : self.longitude,
           'latitude'               : self.latitude,
           'creator_user'           : self.creator_user,
           'sport'                  : self.sport
       }
