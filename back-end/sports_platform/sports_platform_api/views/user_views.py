import re 

from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..controllers.guest import Guest
from ..validation import user_validation


@api_view(['POST'])
def create_user(request):    
    validation = user_validation.User(data=request.data)
    if not validation.is_valid():
        return Response(validation.errors, status=400)
    if 'password' not in request.data:
        return Response('Password must be provided', status=400)
    if 'identifier' not in request.data:
        return Response('Identifier must be provided', status=400)
    password = request.data['password']
    if not(re.search(r'^[a-zA-Z\._\*]*$', password) and (len(password)>=8) and (len(password)<=15)):
        return Response('Password Requirements are not satisfied', status=400)

    try:
        db_data = request.data.copy()
        db_data.update(validation.data) # get validated value if it has
        guest= Guest(db_data['email'], password)
        guest.register(db_data)
    except ValueError:
        return Response('There is an error regarding the provided data', status=400)
    except Exception:
        return Response('There is an internal error, try again later.', status=500)
    return Response(status=201)