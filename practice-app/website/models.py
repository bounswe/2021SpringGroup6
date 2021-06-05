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