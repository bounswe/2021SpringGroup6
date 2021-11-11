from django.db.utils import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..controllers import Guest
from ..models import User
from ..serializers.user_serializer import UserSerializer
from ..validation import user_validation


@api_view(['GET'])
def get_user(request, user_id):
    if not request.user.is_authenticated:
        return Response(data={'message': 'User is not logged in, first you need to login'}, status=401)
    try:
        user = User.objects.get(pk=user_id)
        sports = user.get_sport_skills()
    except User.DoesNotExist:
        return Response(data={"message": 'User id does not exist'}, status=400)
    except Exception:
        return Response(data={'message': 'An error occured, please try again later.'}, status=500)
    
    serialized_user = UserSerializer(user).data
    # drop last_login field that we  do not use
    serialized_user.pop('last_login')
    # add activity stream data
    serialized_user['@context'] = 'https://schema.org/Person'
    serialized_user['@id'] = user.user_id
    serialized_user['sports'] = sports
    if user_id != request.user.user_id:
        pass # TODO here we need to check visibility of the attributes and based on this, we need to remove invisible ones in the future
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
        guest= Guest(db_data['identifier'], password)
        guest.register(db_data)
    except ValueError:
        return Response(data = {"message": 'There is an error regarding the provided data'}, status=400)
    except IntegrityError as e:
        return Response(data = {"message": 'Username is already taken.'}, status=400)
    except Exception:
        return Response(data = {"message": 'There is an internal error, try again later.'}, status=500)
    return Response(status=201)

@api_view(['POST'])
def login(request):
    if request.user.is_authenticated:
        return Response(data= {"message": "Already logged in."}, status=400)

    validation = user_validation.Login(data = request.data)
    if not validation.is_valid():
        return Response(data = {"message": validation.errors}, status=400)

    validated_data = validation.validated_data
    guest = Guest(validated_data['identifier'], validated_data['password'])

    try:
        user = guest.login()
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={"token": token.key},status=200)
        else:
            return Response(data={"message": "Check credentials."}, status=403)
    except Exception as e:
        return Response(data={"message": "Try later."}, status=500)

@api_view(['POST'])
def logout(request):
    
    if not request.user.is_authenticated:
        return Response({"message": "User not logged in."},
                        status=401)
    try:
        request.user.auth_token.delete()
        django.contrib.auth.logout(request)

    except Exception as e:
        return Response({"message": "Try again."},
                        status=500)

    return Response({"message": "Successfully logged out."},
                    status=200)
