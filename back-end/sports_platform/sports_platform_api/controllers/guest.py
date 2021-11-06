from ..models.user_models import User
from django.contrib.auth import authenticate

class Guest:

    def __init__(self, identifier, password):
        self.identifier = identifier
        self.password = password

    def login(self):
        user = authenticate(identifier = self.identifier, password = self.password)
        return user
