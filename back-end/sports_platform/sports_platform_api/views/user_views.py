from django.db.utils import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..controllers.guest import Guest
from ..validation import user_validation


@api_view(['POST'])
def create_user(request):    
    validation = user_validation.User(data=request.data)
    if not validation.is_valid():
        return Response(validation.errors, status=400)
    password = validation.data['password']

    try:
        db_data = request.data.copy()
        db_data.update(validation.data) # get validated value if it has
        guest= Guest(db_data['email'], password)
        guest.register(db_data)
    except ValueError:
        return Response('There is an error regarding the provided data', status=400)
    except IntegrityError:
        return Response('Username is already taken.', status=400)
    except Exception:
        return Response('There is an internal error, try again later.', status=500)
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