from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Equipment
from . import db

views = Blueprint('views', __name__)

@views.route('/equipments', methods=['GET', 'POST'])
@login_required
def post_equipment():
    if request.method == 'POST':
        enteredEquipment = request.form.get('equipment')

        tempEquipment = Equipment.query.filter_by(equipmentName=enteredEquipment).first()
        if tempEquipment:
            flash('Equipment already exists!.', category='error')
        else:
            new_equipment = Equipment(equipmentName=enteredEquipment)
            db.session.add(new_equipment)
            db.session.commit()
            flash('Successfull', category='success')
            return redirect(url_for('views.post_equipment'))


    return render_template("equipments.html", user=current_user)