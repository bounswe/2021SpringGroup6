from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..controllers.guest import Guest
from ..models.user_models import User
from ..serializers.user_serializer import UserSerializer
from ..validation import user_validation
from django.db.utils import IntegrityError


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

@api_view(['POST'])
def create_user(request):    
    validation = user_validation.User(data=request.data)
    if not validation.is_valid():
        return Response(data = {"message": validation.errors}, status=400)
    password = validation.data['password']

    try:
        db_data = request.data.copy()
        db_data.update(validation.data) # get validated value if it has
        guest= Guest(db_data['email'], password)
        guest.register(db_data)
    except ValueError:
        return Response(data = {"message": 'There is an error regarding the provided data'}, status=400)
    except IntegrityError:
        return Response(data = {"message": 'Username is already taken.'}, status=400)
    except Exception:
        return Response(data = {"message": 'There is an internal error, try again later.'}, status=500)
    return Response(status=201)

@api_view(['POST'])
def login(request):
    if request.user.is_authenticated:
        return Response(data= {"message": "Already logged in, logout first."}, status=400)

    validation = user_validation.Login(data = request.data)
    if not validation.is_valid():
        return Response(data = {"message": validation.errors}, status=400)

    validated_data = validation.validated_data
    guest = Guest(validated_data['identifier'], validated_data['password'])

    try:
        user = guest.login()
        if user is not None:
            return Response(status=200)
        else:
            return Response(data={"message": "Check credentials."}, status=403)
    except Exception as e:
        return Response(data={"message": "Try later."}, status=500)
