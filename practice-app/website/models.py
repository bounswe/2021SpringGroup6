from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    date = db.Column(db.Text)
    location = db.Column(db.String())
    creator_user = db.Column(db.String(), db.ForeignKey('user.id'))

    def serialize(self):
       """Return object data in JSON serializable format"""
       return {
           'id'             : self.id,
           'name'           : self.name,
           'date'           : self.date,
           'location'       : self.location,
           'creator_user'   : self.creator_user
       }

