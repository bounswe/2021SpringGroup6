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


@api_view(['GET', 'DELETE'])
def get_equipment(request, equipment_id):
    if request.method == 'GET':
        try:
            equipment = Equipment.objects.get(pk=equipment_id)

            equipment_information = equipment.get_equipment()

            print(equipment_information)

            return Response(data = equipment_information, status=200)
        except Equipment.DoesNotExist:
            return Response(data={"message": 'Equipment id does not exist'}, status=400)
        except Exception:
            return Response(data={'message': 'An error occured, please try again later.'}, status=500)

    elif request.method == 'DELETE':
        if not request.user.is_authenticated:
            return Response({"message": "User not logged in."},
                            status=401)
        try:
            equipment = Equipment.objects.get(equipment_id=equipment_id)

            if equipment.creator.user_id != request.user.user_id:
                return Response(data={"message": "Only creators can delete equipments."}, status=403)

            with transaction.atomic():
                equipment.delete()
            return Response(status=204)

        except Equipment.DoesNotExist:
            return Response(data={"message": "Try with a valid equipment."}, status=400)
        except Exception:
            return Response(data={"message": 'Try later.'}, status=500)


@api_view(['POST'])
def search_equipment(request):
    validation = equipment_validation.Search(data=request.data)

    if not validation.is_valid():
        return Response(data={"message": validation.errors}, status=400)

    try:
        validated_body = validation.validated_data
        equipments = Equipment.search(validated_body)
        return Response(equipments, status=200)
    except:
        return Response(data={"message": 'Try later.'}, status=500)


@api_view(['POST', 'GET'])
def post_equipment_post(request, equipment_id):

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({"message": "User not logged in."},
                            status=401)

        user = request.user

        validation = equipment_validation.EquipmentDiscussionPost(data=request.data)

        if not validation.is_valid():
            return Response(data={"message": validation.errors}, status=400)

        try:
            res = EquipmentDiscussionPost.create_post(
                validation.validated_data, user, equipment_id)

            if res == 500:
                return Response(data={"message": "Try later."}, status=500)
            if res == 402:
                return Response(data={"message": "Try with a valid equipment."}, status=400)
            else:
                return Response(data=res, status=201)
        except Exception as e:
            return Response(data={"message": 'Try later.'}, status=500)

    if request.method == 'GET':
        if not request.user.is_authenticated:
            return Response({"message": "User not logged in."},
                            status=401)

        user = request.user

        try:
            equipment = Equipment.objects.get(equipment_id=equipment_id)

            res = equipment.get_posts()

            if res == 500:
                return Response(data={"message": "Try later."}, status=500)
            else:
                return Response(data=res, status=200)
        except Equipment.DoesNotExist:
            return Response(data={"message": "Try with a valid equipment."}, status=400)
        except Exception as e:
            return Response(data={"message": 'Try later.'}, status=500)


@api_view(['DELETE', 'POST'])
def delete_equipment_post(request, equipment_id, post_id):

    if request.method == 'DELETE':
        if not request.user.is_authenticated:
            return Response({"message": "User not logged in."},
                            status=401)

        user = request.user

        try:
            post = EquipmentDiscussionPost.objects.get(post_id=post_id)

            if post.equipment.equipment_id != equipment_id:
                return Response(data={"message": "This post does not belong to that equipment_id."}, status=400)

            if user.user_id != post.equipment.creator.user_id and user.user_id != post.author.user_id:
                return Response(data={"message": "Only post authors and equipment creators can delete posts."}, status=400)

            try:
                with transaction.atomic():
                    post.delete()
                return Response(status=204)
            except:
                return Response(data={"message": "Try later."}, status=500)

        except EquipmentDiscussionPost.DoesNotExist:
            return Response(data={"message": "Try with a valid discussion post."}, status=400)
        except Exception as e:
            return Response(data={"message": 'Try later.'}, status=500)

    if request.method == 'POST':

        if not request.user.is_authenticated:
            return Response({"message": "User not logged in."},
                            status=401)

        user = request.user

        validation = equipment_validation.EquipmentDiscussionComment(
            data=request.data)
        if not validation.is_valid():
            return Response(data={"message": validation.errors}, status=400)

        try:
            post = EquipmentDiscussionPost.objects.get(post_id=post_id)

            if post.equipment.equipment_id != equipment_id:
                return Response(data={"message": "This post does not belong to that equipment_id."}, status=400)

            res = post.comment_post(validation.validated_data, user)

            if res == 500:
                return Response(data={"message": "Try later."}, status=500)

            else:
                return Response(status=201)
        except EquipmentDiscussionPost.DoesNotExist:
            return Response(data={"message": "Try with a valid post."}, status=400)
        except Exception as e:
            return Response(data={"message": 'Try later.'}, status=500)


@api_view(['DELETE'])
def delete_equipment_comment(request, equipment_id, post_id, comment_id):

    if not request.user.is_authenticated:
        return Response({"message": "User not logged in."},
                        status=401)

    user = request.user

    try:
        comment = EquipmentDiscussionComment.objects.get(comment_id=comment_id)

        if comment.post.equipment.equipment_id != equipment_id:
            return Response(data={"message": "This comment does not belong to that equipment_id."}, status=400)

        if comment.post.post_id != post_id:
            return Response(data={"message": "This comment does not belong to that post_id."}, status=400)

        if user.user_id != comment.post.equipment.creator.user_id and user.user_id != comment.author.user_id:
            return Response(data={"message": "Only comment authors and equipment creators can delete posts."}, status=400)

        try:
            with transaction.atomic():
                comment.delete()
            return Response(status=204)
        except:
            return Response(data={"message": "Try later."}, status=500)

    except EquipmentDiscussionComment.DoesNotExist:
        return Response(data={"message": "Try with a valid discussion comment."}, status=400)
    except Exception as e:
        return Response(data={"message": 'Try later.'}, status=500)
