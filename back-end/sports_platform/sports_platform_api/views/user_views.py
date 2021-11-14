from django.db.utils import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..controllers.guest import Guest
from ..validation import user_validation
from django.contrib.auth.decorators import login_required
from ..models import User
from ..controllers import Guest
import re
from rest_framework.authtoken.models import Token
import django.contrib.auth 


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
    except IntegrityError:
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


@api_view(['POST'])
def forgot_password(request):

    if request.user.is_authenticated:
        return Response({"message": "Already logged in use change password on settings instead."},
                        status=401)

    validation = user_validation.Recover(data=request.data)
    
    if not validation.is_valid():
        return Response(data={"message": validation.errors}, status=400)

    try:
        validated_data = validation.validated_data
        guest = Guest(None, None)

        res = guest.forget_password(validated_data['email'])

        if res == 100:
            # No user with email
            return Response({"message": "If email provided is correct, a reset password is sent, please check spam."},
                            status=200)
        elif res == 500:
            return Response({"message": "Try again."},
                            status=500)

    except Exception as e:
        print(e)
        return Response({"message": "Try again."},
                        status=500)

    return Response({"message": "If email provided is correct, a reset password is sent, please check spam."},
                    status=200)
