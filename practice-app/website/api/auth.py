from flask import Blueprint, render_template, request, flash, redirect, url_for
from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

# endpoint for User Login
# filters by email; if email does not exists, gives error
# if email exists, checks password; if does not match, gives error
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

# endpoint for User Logout
# logs out using imported logout_user function
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# endpoint for User Sign-up
# gets the necessary inputs, checks if email exists
# checks several steps, if does not fit, gives error
# if no error, then creates new user by entered inputs, adds to the database
# generate hash for password using sha266
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4:
            flash('Email must be greater that 4 chars.', category='error')
        elif len(first_name) < 2:
            flash('First name must be grater than 1 chars.', category='error')
        elif password1 != password2:
            flash('Passwords are not same!', category='error')
        elif len(password1) < 8:
            flash('Minimum Password length is 8 chars', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Successful', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
