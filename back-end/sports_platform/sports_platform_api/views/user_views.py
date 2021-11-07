from django.contrib.auth.hashers import identify_hasher
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..validation import user_validation
from ..models import User
from ..controllers import Guest


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

@api_view(['POST'])
def follow_user(request, user_id):

    current_user = request.user

    if not current_user.is_authenticated:
        return Response(data={"message": "Login required."}, status=403)
    
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


@api_view(['POST'])
def unfollow_user(request, user_id):

    current_user = request.user

    if not current_user.is_authenticated:
        return Response(data={"message": "Login required."}, status=403)
    
    if current_user.user_id != user_id:
        return Response(data={"message": "Not allowed to unfollow for another user."}, status=403)

    validation = user_validation.Follow(data=request.data)
    if not validation.is_valid():
        return Response(validation.errors, status=400)
    
    user_to_follow = validation.validated_data['user_id']

    try:
        res = current_user.unfollow(user_to_follow)

        if res == 403:
            return Response(data={"message": "Enter a valid user_id to unfollow."}, status=400)  
        elif res == 500:
            return Response(data={"message": "Try later."}, status=500)
        else:
            return Response(status=200) 

    except Exception as e:
        return Response(data=str(e), status=500)  