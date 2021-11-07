from django.contrib.auth import authenticate
from ..models.user_models import User

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
