from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Equipment, EquipmentDiscussionPost, EquipmentDiscussionComment
from ..validation import equipment_validation


@api_view(['POST'])
def create_equipment(request):

    if not request.user.is_authenticated:
        return Response({"message": "User not logged in."},
                        status=401)

    creator = request.user

    validation = equipment_validation.Equipment(data=request.data)

    if not validation.is_valid():
        return Response(data={"message": validation.errors}, status=400)

    validated_body = validation.validated_data
    validated_body['creator'] = creator

    try:
        res = Equipment.create_equipment(validated_body, creator)

        if res == 102:
            return Response(data={"message": 'Enter a valid sport.'}, status=400)
        elif res == 500:
            return Response(data={"message": 'Try Later.'}, status=500)

        response = dict()
        response['@context'] = 'https://schema.org/Product'
        response['@id'] = res['@id']

        return Response(data=response, status=201)

    except Exception as e:
        print(e)
        return Response(data={"message": 'There is an internal error, try again later.'}, status=500)
