from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    price = db.Column(db.String(150))

    def serialize(self):
       """Return object data in JSON serializable format"""
       return {
           'id'                     : self.id,
           'name'                   : self.name,
           'price'                  : self.price,
       }
    
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

class Interesteds(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    
    def serialize(self):
        """Return object data in JSON serializable format"""
        return {
            'event_id'              : self.event_id,
            'user_id'               : self.user_id
        }

class Spectators(db.Model):   
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    
    def serialize(self):
        """Return object data in JSON serializable format"""
        return {
            'event_id'              : self.event_id,
            'user_id'               : self.user_id
        }


# Corresponds to a discussion page for an event
class DiscussionPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)

    def serialize(self):
       """Return object data in JSON serializable format"""
       return {
           'id'                     : self.id,
           'text'                   : self.text
       }


class Sport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sport = db.Column(db.Text)

    def serialize(self):
       """Return object data in JSON serializable format"""
       return {
           'id'                     : self.id,
           'sport'                   : self.sport
       }