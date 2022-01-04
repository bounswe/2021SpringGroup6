from django.test import Client, TestCase
from ..models import Equipment, EquipmentDiscussionPost, EquipmentDiscussionComment, Sport
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .test_helper_functions import create_mock_user
from datetime import datetime, timezone


class EquipmentDiscussionTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.maxDiff = None

        lion_info = {'identifier': 'lion',
                     'password': 'roarroar', 'email': 'lion@roar.com'}
        cat_info = {'identifier': 'cat',
                    'password': 'meowmeow', 'email': 'cat@meow.com'}
        dog_info = {'identifier': 'dog',
                    'password': 'barkbark', 'email': 'dog@bark.com'}

        self.lion_user = create_mock_user(lion_info)
        self.cat_user = create_mock_user(cat_info)
        self.dog_user = create_mock_user(dog_info)

        self.lion_token, _ = Token.objects.get_or_create(user=self.lion_user)
        self.cat_token, _ = Token.objects.get_or_create(user=self.cat_user)
        self.dog_token, _ = Token.objects.get_or_create(user=self.dog_user)

        authenticate(identifier=self.lion_user.identifier,
                     password=self.lion_user.password)
        authenticate(identifier=self.cat_user.identifier,
                     password=self.cat_user.password)
        authenticate(identifier=self.dog_user.identifier,
                     password=self.dog_user.password)

        equipment_info1 = {
            "name": "soccer ball",
            "sport": "soccer",
            "latitude": 41.002697,
            "longitude": 39.716763,
            "description": "soccer ball at Trabzon"
        }


        Sport.objects.create(name="soccer")

        self.equipment1 = Equipment.create_equipment(
            equipment_info1, self.lion_user)
        self.equipment1 = Equipment.objects.get(
            equipment_id=self.equipment1['@id'])

        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()

        self.post1 = EquipmentDiscussionPost.objects.create(
            equipment=self.equipment1, author=self.cat_user, text="My First Post", dateCreated=dt)
        utc_dt = datetime.now(timezone.utc)  # UTC time
        dt = utc_dt.astimezone()
        self.post2 = EquipmentDiscussionPost.objects.create(
            equipment=self.equipment1, author=self.lion_user, text="My Second Post", dateCreated=dt)

        self.comment1 = EquipmentDiscussionComment.objects.create(
            post=self.post1, author=self.dog_user, text="Comment To First Post", dateCreated=dt)

        self.post_body = {
            "sharedContent": "https://shorturl.at/vxHI3",
            "text": "I added the photo of the equipment"
        }

        self.comment_body = {
            "text": "Equipment looks great"
        }

        self.request_param = {'post_success': self.equipment1.equipment_id,
                              'comment_success': [self.equipment1.equipment_id, self.post1.post_id],
                              'delete_post_by_creator': [self.equipment1.equipment_id, self.post1.post_id],
                              'delete_post_by_author': [self.equipment1.equipment_id, self.post1.post_id],
                              'delete_comment': [self.equipment1.equipment_id, self.post1.post_id, self.comment1.comment_id],
                              'cannot_delete': [self.equipment1.equipment_id, self.post1.post_id, self.comment1.comment_id],
                              'get_posts': self.equipment1.equipment_id,
                              'wrong_equipment_id': [self.equipment1.equipment_id+1, self.post1.post_id]
                              }

        self.request_token = {'post_success': self.dog_token,
                              'comment_success': self.cat_token,
                              'delete_post_by_creator': self.lion_token,
                              'delete_post_by_author': self.cat_token,
                              'delete_comment': self.dog_token,
                              'cannot_delete': self.cat_token,
                              'get_posts': self.lion_token,
                              'wrong_equipment_id': self.lion_token,
                              }

        self.response_bodies = {'cannot_delete': {"message": "Only comment authors and equipment creators can delete posts."},
                                'wrong_equipment_id': {"message": "This post does not belong to that equipment_id."},
                                'get_posts': {
                                    "@context": "https://schema.org/Product",
                                    "@id": self.equipment1.equipment_id,
                                    "additionalProperty": {
                                        "@type": "PropertyValue",
                                        "name": "posts",
                                        "value": [{
                                            "@context": "https://schema.org/SocialMediaPosting",
                                            "@id": self.post1.post_id,
                                            "author": {
                                                "@context": "https://schema.org/Person",
                                                "@id": self.post1.author.user_id,
                                                "identifier": self.post1.author.identifier
                                            },
                                            "text": self.post1.text,
                                            "dateCreated": self.post1.dateCreated,
                                            "comment": [
                                                {
                                                    "@context": "https://schema.org/Comment",
                                                    "@id": self.comment1.comment_id,
                                                    "author": {
                                                        "@context": "https://schema.org/Person",
                                                        "@id": self.comment1.author.user_id,
                                                        "identifier": self.comment1.author.identifier
                                                    },
                                                    "text": self.comment1.text,
                                                    "dateCreated": self.comment1.dateCreated,
                                                }
                                            ]
                                        },
                                            {
                                            "@context": "https://schema.org/SocialMediaPosting",
                                            "@id": self.post2.post_id,
                                            "author": {
                                                "@context": "https://schema.org/Person",
                                                "@id": self.post2.author.user_id,
                                                "identifier": self.post2.author.identifier
                                            },
                                            "text": self.post2.text,
                                            "dateCreated": self.post2.dateCreated,
                                            "comment": []
                                        }

                                        ]
                                    }
        },
        }

    def test_post_success(self):
        test_type = 'post_success'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/equipments/" + str(request_param) + "/discussion"

        response = self.client.post(
            path, self.post_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 201)
        self.assertTrue(EquipmentDiscussionPost.objects.filter(
            equipment=self.equipment1, author=self.dog_user.user_id).exists())

    def test_comment_success(self):
        test_type = 'comment_success'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/equipments/" + \
            str(request_param[0]) + "/discussion/" + str(request_param[1])

        response = self.client.post(
            path, self.comment_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 201)
        self.assertTrue(EquipmentDiscussionComment.objects.filter(
            author=self.cat_user, post=self.post1).exists())

    def test_delete_post_by_creator(self):
        test_type = 'delete_post_by_creator'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/equipments/" + \
            str(request_param[0]) + "/discussion/" + str(request_param[1])

        response = self.client.delete(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 204)
        self.assertFalse(EquipmentDiscussionPost.objects.filter(
            post_id=self.post1.post_id).exists())

    def test_delete_post_by_author(self):
        test_type = 'delete_post_by_author'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/equipments/" + \
            str(request_param[0]) + "/discussion/" + str(request_param[1])

        response = self.client.delete(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 204)
        self.assertFalse(EquipmentDiscussionPost.objects.filter(
            post_id=self.post1.post_id).exists())

    def test_delete_comment(self):
        test_type = 'delete_comment'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/equipments/" + str(request_param[0]) + "/discussion/" + str(
            request_param[1]) + "/comment/" + str(request_param[2])

        response = self.client.delete(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 204)
        self.assertFalse(EquipmentDiscussionComment.objects.filter(
            comment_id=self.comment1.comment_id).exists())

    def test_cannot_delete(self):
        test_type = 'cannot_delete'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/equipments/" + str(request_param[0]) + "/discussion/" + str(
            request_param[1]) + "/comment/" + str(request_param[2])

        response = self.client.delete(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertEqual(response.status_code, 400)

    def test_get_posts(self):
        test_type = 'get_posts'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/equipments/" + str(request_param) + "/discussion"

        response = self.client.get(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertEqual(response.status_code, 200)

    def test_wrong_equipment_id(self):
        test_type = 'wrong_equipment_id'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/equipments/" + \
            str(request_param[0]) + "/discussion/" + str(request_param[1])

        response = self.client.post(
            path, self.post_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertEqual(response.status_code, 400)
