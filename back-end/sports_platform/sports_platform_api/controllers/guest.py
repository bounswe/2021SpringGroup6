from django.contrib.auth import authenticate
from ..models.user_models import User
import string
import random
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings
from django.db import IntegrityError, transaction

class Guest:

    def __init__(self, identifier, password):
        self.identifier = identifier
        self.password = password

    def login(self):
        user = authenticate(identifier = self.identifier, password = self.password)
        return user
    
    def register(self, info):
        register_info = {k:v for k,v in info.items() if k!='sports'}
        try:
            user = User.objects.create_user(**register_info)
            user.save()
        except Exception as e:
            raise e
        
        if 'sports' in info:
            try:
                for skills in info['sports']:
                    user.add_sport_interest(skills['sport'], skills['skill_level'])
            except Exception as e:
                raise e
        return user

    def forget_password(self, email):

        try: 
            user = User.objects.filter(email=email)
        except Exception as e:
            return 500

        if len(user) == 0:
            return 100

        user = user[0]

        new_pass = generate_random_password()
        hashed_pass = make_password(new_pass)

        try:
            with transaction.atomic():
                user.password = hashed_pass
                user.save()

                send_mail(subject='New Password for your Squad Game Account',
                          message=f"Your new password for the account with username {user.identifier} is {new_pass}, you can login using this password and change it on settings.",
                          from_email=settings.EMAIL_HOST_USER,
                          recipient_list=[user.email])
            return 200
        except Exception as e:
            return 500
            


def generate_random_password():

    characters = list(string.ascii_letters + string.digits + ".*")
    random.shuffle(characters)

    password = []
    for i in range(15):
        password.append(random.choice(characters))

    random.shuffle(password)
    return "".join(password)
