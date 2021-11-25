from django.db import transaction
from django.db.utils import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
import django.contrib.auth 
from ..controllers import Guest
from ..models import User, SportSkillLevel
from ..serializers.user_serializer import UserSerializer
from ..validation import user_validation
import django.contrib.auth

@api_view(['GET', 'PUT'])
def get_user(request, user_id):
    if request.method == 'GET':
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
        serialized_user['@type'] = 'Person'
        serialized_user['knowsAbout'] = sports
        
        if (request.user.is_authenticated) and (user_id == request.user.user_id):
            return Response(serialized_user,status=200)
        else:
        # TODO here we need to check visibility of the attributes and based on this, we need to remove invisible ones in the future
            return Response(serialized_user,status=200)  
    elif request.method == 'PUT':
        if not request.user.is_authenticated:
            return Response({"message": "Login required."},
                        status=401)
        validation = user_validation.Update(data=request.data)
        if not validation.is_valid():
            return Response(data = {"message": validation.errors}, status=400)
        try:
            sport_data = validation.data['sports'] if 'sports' in validation.data else None
            update_info = {k:v for k,v in validation.data.items() if k!='sports'}
            with transaction.atomic():
                request.user.update(sport_data, update_info)
            return Response(status=200)
        except Exception:
            return Response(data={'message': 'An error occured, please try again later.'}, status=500)
             
        

@api_view(['POST'])
def create_user(request):    
    validation = user_validation.User(data=request.data)
    if not validation.is_valid():
        return Response(data = {"message": validation.errors}, status=400)
    password = validation.data['password']

    try:
        guest= Guest(validation.data['identifier'], password)
        with transaction.atomic():
            guest.register(validation.data)
    except ValueError:
        return Response(data = {"message": 'There is an error regarding the provided data'}, status=400)
    except IntegrityError as e:
        if 'sport' in str(e.__cause__):
            response_message = 'Given sport is not supported.'
        elif 'identifier' in str(e.__cause__):
            response_message = 'Username is already taken'
        elif 'email' in str(e.__cause__):
            response_message = 'Email is already taken'
        else:
            response_message = 'There is an integrity error.'
        
        return Response(data = {"message": response_message}, status=400)
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
            return Response(data={"token": token.key, "user_id": user.user_id},status=200)
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


@api_view(['POST', 'DELETE', 'GET'])
def follow_user(request, user_id):

    if request.method == 'POST':

        current_user = request.user

        if not current_user.is_authenticated:
            return Response(data={"message": "Login required."}, status=401)
        
        if current_user.user_id != user_id:
            return Response(data={"message": "Not allowed to follow for another user."}, status=403)

        validation = user_validation.Follow(data=request.data)
        if not validation.is_valid():
            return Response(validation.errors, status=400)
        
        user_to_follow = validation.validated_data['user_id']

        if user_to_follow == current_user.user_id:
            return Response(data={"message": "User cannot follow itself."}, status=400)

        try:
            res = current_user.follow(user_to_follow)

            if res == 401:
                return Response(data={"message": "Enter a valid user_id to follow."}, status=400)
            elif res == 402:
                return Response(data={"message": "User already followed."}, status=400)
            elif res == 500:
                return Response(data={"message": "Try later."}, status=500)
            else:
                return Response(status=200)

        except Exception as e:
            return Response(data=str(e), status=500)

    elif request.method == 'DELETE':
        current_user = request.user

        if not current_user.is_authenticated:
            return Response(data={"message": "Login required."}, status=401)

        if current_user.user_id != user_id:
            return Response(data={"message": "Not allowed to unfollow for another user."}, status=403)

        validation = user_validation.Follow(data=request.data)
        if not validation.is_valid():
            return Response(validation.errors, status=400)

        user_to_unfollow = validation.validated_data['user_id']

        try:
            res = current_user.unfollow(user_to_unfollow)

            if res == 403:
                return Response(data={"message": "Enter a valid user_id to unfollow."}, status=400)
            elif res == 500:
                return Response(data={"message": "Try later."}, status=500)
            else:
                return Response(status=200)

        except Exception as e:
            return Response(data={"message": "Try later."}, status=500)

    elif request.method == 'GET':

        current_user = request.user

        if not current_user.is_authenticated:
            return Response(data={"message": "Login required."}, status=401)

        try:
            user_following = User.objects.get(user_id=user_id)

            following = user_following.get_following()

            if following == 500:
                return Response(data={"message": "Try later."}, status=500)
            else:
                return Response(data=following, status=200)
        except User.DoesNotExist:
            return Response(data={"message": "User does not exist."}, status=400)
        except Exception as e:
            return Response(data={"message": "Try later."}, status=500)

        

@api_view(['GET'])
def get_follower(request, user_id):

    current_user = request.user

    if not current_user.is_authenticated:
        return Response(data={"message": "Login required."}, status=401)

    try:
        user_followed = User.objects.get(user_id=user_id)

        follower = user_followed.get_follower()

        if follower == 500:
            return Response(data={"message": "Try later."}, status=500)
        else:
            return Response(data=follower, status=200)
    except User.DoesNotExist:
        return Response(data={"message": "User does not exist."}, status=400)
    except Exception as e:
        return Response(data={"message": "Try later."}, status=500)



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
        return Response({"message": "Try again."},
                        status=500)

    return Response({"message": "If email provided is correct, a reset password is sent, please check spam."},
                    status=200)

@api_view(['PUT'])
def set_visibility(request, user_id):
    current_user = request.user
    if not current_user.is_authenticated:
        return Response(data={"message": "Login required."}, status=401)
    if current_user.user_id != int(user_id):
        return Response(data={"message": "Users cannot change other users' visibility information"}, status=403)

    validation = user_validation.Set_Visibility(data=request.data)
    if not validation.is_valid():
        return Response(data={"message": validation.errors}, status=400)
    try:
        with transaction.atomic():
            current_user.set_visibility(validation.validated_data)
            return Response(status=200)
    except Exception:
        return Response(data={'message': 'An error occured, please try again later.'}, status=500)

@api_view(['POST', 'DELETE'])
def block_user(request, user_id):

    if request.method == 'POST':
        current_user = request.user
        if not current_user.is_authenticated:
            return Response(data={"message": "Login required."}, status=401)
        
        if current_user.user_id != user_id:
            return Response(data={"message": "Not allowed to block for another user."}, status=403)

        validation = user_validation.Block(data=request.data)
        if not validation.is_valid():
            return Response(validation.errors, status=400)
        
        user_to_block= validation.validated_data['user_id']

        if user_to_block == current_user.user_id:
            return Response(data={"message": "User cannot block itself."}, status=400)

        try:
            res = current_user.block(user_to_block)
            if res == 401:
                return Response(data={"message": "Enter a valid user_id to block."}, status=400)
            elif res == 402:
                return Response(data={"message": "User already blocked."}, status=400)
            elif res == 500:
                return Response(data={"message": "An error occured, please try again later."}, status=500)
            else:
                return Response(status=200)
        except Exception as e:
            return Response(data={'message': 'An error occured, please try again later.'}, status=500)