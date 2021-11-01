from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..validation import user_validation
from ..controllers.guest import Guest
import re 

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
        return Response(data='Password Requirments are not satisfied', status=400)

    try:
        guest= Guest(request.data['email'], password)
        guest.register(request.data)
    except ValueError as e:
        return Response(data=str(e), status=400)
    except Exception as e:
        return Response(data=str(e), status=500)
    return Response(status=201)