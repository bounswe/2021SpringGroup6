from django.contrib.auth.decorators import login_required
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models.user_models import User, SportSkillLevel
from ..serializers.user_serializer import UserSerializer

@api_view(['GET'])
def get_user(request, user_id):
    try:    
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response('User id does not exist', status=400)
    except Exception:
        return Response('An error occured, please try again later.', status=500)
    
    try:
        sports = User.objects.filter(email='1@s.com')
        print(type(sports))
        print(sports)
    except:
        pass
    serialized_user = UserSerializer(user).data
    # drop last_login field that we  do not use
    serialized_user.pop('last_login')
    # add activity stream data
    serialized_user['@context'] = 'https://schema.org/Person'
    serialized_user['@id'] = user.user_id
    return Response(serialized_user,status=200)