from django.contrib.auth.hashers import identify_hasher
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..validation import user_validation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from ..models import User
from ..controllers import Guest
import re


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

    