from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

@views.route('create_equipment/', methods=['POST','GET'])
@login_required
def create_equipment():
    if request.method == 'POST':
        equipment = {
            "name" : request.form.get("name")
        }

        req = "http://127.0.0.1:5000/api/v1.0/equipments/"
        headers = {'Content-type': 'application/json'}
        response = requests.post(req, data=json.dumps(equipment), headers=headers)

        if response.status_code == 201:
            flash('Equipment Created', category='success')
            return redirect(url_for('views.home'))
        elif response.status_code == 400 :
            flash('Check Information Entered', category='error')
        elif response.status_code == 409 :
            flash('Equipment Already Exists!', category='error')
        else:
            flash('Error Occured, Try Again Later', category='error')
    
    return render_template("equipments.html", user=current_user)
    
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

