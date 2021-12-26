from django.db import transaction
import django.contrib.auth 
from django.db.utils import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sports_platform_api.models.user_models import Notification
from ..controllers import Guest
from ..helpers import filter_visibility
from ..models import User,Block
from ..serializers.user_serializer import UserSerializer
from ..validation import user_validation

@api_view(['GET', 'PUT', 'DELETE'])
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
        # add activity stream data
        serialized_user['@context'] = 'https://schema.org/Person'
        serialized_user['@id'] = user.user_id
        serialized_user['@type'] = 'Person'
        serialized_user['knowsAbout'] = sports
        
        if (request.user.is_authenticated) and (user_id == request.user.user_id):
            return Response(serialized_user,status=200)
        elif request.user.is_authenticated:
            blocks = Block.objects.filter(blocker=user, blocked=request.user)
            if not blocks.exists():
                return Response(serialized_user,status=200)
            else:
                return Response({"message": "This user cannot see requested user."},status=403)
        else:
            serialized_user = filter_visibility(user.__dict__, serialized_user)
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
    elif request.method == 'DELETE':
        if not request.user.is_authenticated:
            return Response({"message": "User not logged in."},
                        status=401)
        
        if user_id != request.user.user_id:
            return Response(data={"message": "User cannot delete others' accounts."}, status=400)

        try:
            with transaction.atomic():
                request.user.delete()
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
            return Response(data={"message": "Try later."}, status=500)

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

@api_view(['POST', 'DELETE', 'GET'])
def block_user(request, user_id):
    current_user = request.user
    if request.method == 'POST':
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
   

    elif request.method == 'DELETE':   
        if not current_user.is_authenticated:
            return Response(data={"message": "Login required."}, status=401)

        if current_user.user_id != user_id:
            return Response(data={"message": "Not allowed to unblock for another user."}, status=403)

        validation = user_validation.Block(data=request.data)
        if not validation.is_valid():
            return Response(validation.errors, status=400)
            
        user_to_unblock= validation.validated_data['user_id']

        if user_to_unblock == current_user.user_id:
            return Response(data={"message": "User cannot unblock itself."}, status=400)

        try:
            res = current_user.unblock(user_to_unblock)
            if res == 403:
                return Response(data={"message": "Enter a valid user_id to unblock."}, status=400)
            elif res == 500:
                return Response(data={"message": "An error occured, please try again later"}, status=500)
            else:
                return Response(status=200)
        except Exception:
            return Response(data={'message': 'An error occured, please try again later.'}, status=500)
    
    elif request.method == 'GET':
        if not current_user.is_authenticated:
            return Response(data={"message": "Login required."}, status=401)

        try:
            user_blocked = User.objects.get(user_id=user_id)

            blocked = user_blocked.get_blocked()

            if blocked == 500:
                return Response(data={"message": "Try later."}, status=500)
            else:
                return Response(data=blocked, status=200)
        except User.DoesNotExist:
            return Response(data={"message": "User does not exist."}, status=400)
        except Exception as e:
            return Response(data={"message": "Try later."}, status=500)


@api_view(['GET'])
def get_participating_events(request, user_id):

    current_user = request.user

    if not current_user.is_authenticated:
        return Response(data={"message": "Login required."}, status=401)

    try:
        user = User.objects.get(user_id=user_id)

        events = user.get_participating_events()

        if events == 500:
            return Response(data={"message": "Try later."}, status=500)
        else:
            return Response(data=events, status=200)
    except User.DoesNotExist:
        return Response(data={"message": "User does not exist."}, status=400)
    except Exception as e:
        return Response(data={"message": "Try later."}, status=500)


@api_view(['GET'])
def get_interested_events(request, user_id):

    current_user = request.user

    if not current_user.is_authenticated:
        return Response(data={"message": "Login required."}, status=401)

    try:
        user = User.objects.get(user_id=user_id)

        events = user.get_interested_events()

        if events == 500:
            return Response(data={"message": "Try later."}, status=500)
        else:
            return Response(data=events, status=200)
    except User.DoesNotExist:
        return Response(data={"message": "User does not exist."}, status=400)
    except Exception as e:
        return Response(data={"message": "Try later."}, status=500)


@api_view(['GET'])
def get_spectating_events(request, user_id):

    current_user = request.user

    if not current_user.is_authenticated:
        return Response(data={"message": "Login required."}, status=401)

    try:
        user = User.objects.get(user_id=user_id)

        events = user.get_spectating_events()

        if events == 500:
            return Response(data={"message": "Try later."}, status=500)
        else:
            return Response(data=events, status=200)
    except User.DoesNotExist:
        return Response(data={"message": "User does not exist."}, status=400)
    except Exception as e:
        return Response(data={"message": "Try later."}, status=500)


@api_view(['GET','POST'])
def get_badges(request, user_id):

    if request.method == 'GET':
        try:
            user = User.objects.get(user_id=user_id)

            badges = user.get_badges()

            if badges == 500:
                return Response(data={"message": "Try later."}, status=500)
            else:
                return Response(data=badges, status=200)
        except User.DoesNotExist:
            return Response(data={"message": "User does not exist."}, status=400)
        except Exception as e:
            return Response(data={"message": "Try later."}, status=500)

    elif request.method == 'POST':

        current_user = request.user

        if not current_user.is_authenticated:
            return Response(data={"message": "Login required."}, status=401)

        try:

            validation = user_validation.Badge(data=request.data)
            if not validation.is_valid():
                return Response(validation.errors, status=400)

            badge = validation.validated_data['badge']

            if user_id == current_user.user_id:
                return Response(data={"message": "Users cannot give badge to themselves."}, status=400)

            badges = current_user.give_badge(user_id, badge)

            if badges == 401:
                return Response(data={"message": "Enter a valid badge."}, status=400)
            elif badges == 402:
                return Response(data={"message": "Enter a valid user."}, status=400)
            elif badges == 403:
                return Response(data={"message": "Already gave this badge to this user."}, status=400)
            elif badges == 500:
                return Response(data={"message": "Try later."}, status=500)
            else:
                return Response(status=201)
        except Exception as e:
            return Response(data={"message": "Try later."}, status=500)    

@api_view(['GET'])
def notification(request):
    current_user = request.user

    if not current_user.is_authenticated:
        return Response(data={"message": "Login required."}, status=401)

    try:  
        notifications=current_user.get_notifications()
    except Exception:
            return Response(data={"message": "Try later."}, status=500)    
    return Response(data=notifications, status=200)

@api_view(['POST'])
def read_notification(request, notification_id):
    if not request.user.is_authenticated:
        return Response(data={"message": "Login required."}, status=401)

    try:
        notification = Notification.objects.get(id=notification_id)
        if request.user.user_id != notification.user_id.user_id:
            return Response(data={"message": "Not allowed to read notifications of another user."}, status=403)
        notification.read = True
        notification.save()
        return Response(status=200)
    except Notification.DoesNotExist:
        return Response(data={"message": "Notification does not exist."}, status=400)
    except Exception:
        return Response(data={"message": "Try later."}, status=500)    
            

@api_view(['POST'])
def search_user(request):
    validation = user_validation.Search(data=request.data)

    if not validation.is_valid():
        return Response(data={"message": validation.errors}, status=400)

    validated_body = validation.validated_data
    block_check = False
    user = None
    if (request.user.is_authenticated):
        block_check = True
        user = request.user
    try:
        users = User.search_user(validated_body, block_check, user)
    except:
        return Response(data={"message": "Try later."}, status=500)
    response = {'@context':"https://www.w3.org/ns/activitystreams", 'type':'Collection',
    'total_items':len(users),'items':[]}
    try:
        for returned_user in users:
            serialized_user = UserSerializer(returned_user).data
            sports = returned_user.get_sport_skills()
            serialized_user['@context'] = 'https://schema.org/Person'
            serialized_user['@id'] = returned_user.user_id
            serialized_user['@type'] = 'Person'
            serialized_user['knowsAbout'] = sports
            response['items'].append(serialized_user)
    except:
        return Response(data={"message": "Try later."}, status=500)
    return Response(response, status=200)
