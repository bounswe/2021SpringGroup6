from django.test import Client, TestCase
from ..models import Follow
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .test_helper_functions import create_mock_user


class FollowTest(TestCase):

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

        Follow.objects.create(follower=self.lion_user, following=self.cat_user)
        Follow.objects.create(follower=self.lion_user, following=self.dog_user)

        self.request_param = {'follow_success': self.cat_user.user_id,
                              'follow_for_other': self.dog_user.user_id,
                              'get_follower': self.cat_user.user_id,
                              'already_followed': self.lion_user.user_id,
                              'follow_yourself': self.cat_user.user_id,
                              'follow_non_existing': self.cat_user.user_id,
                              'get_following': self.lion_user.user_id,
                              'unfollow_success': self.lion_user.user_id,
                              'unfollow_for_other': self.lion_user.user_id,
                              'unfollow_non_following': self.cat_user.user_id,
                              }

        self.request_user_id = {'follow_success': self.dog_user.user_id,
                                'follow_for_other': self.lion_user.user_id,
                                'already_followed': self.dog_user.user_id,
                                'follow_yourself': self.cat_user.user_id,
                                'follow_non_existing': 576,
                                'get_following': self.cat_user.user_id,
                                'unfollow_success': self.cat_user.user_id,
                                'unfollow_for_other': self.dog_user.user_id,
                                'unfollow_non_following': self.dog_user.user_id,
                                }

        self.request_token = {'follow_success': self.cat_token,
                              'follow_for_other': self.cat_token,
                              'get_follower': self.lion_token,
                              'already_followed': self.lion_token,
                              'follow_yourself': self.cat_token,
                              'follow_non_existing': self.cat_token,
                              'get_following': self.cat_token,
                              'unfollow_success': self.lion_token,
                              'unfollow_for_other': self.cat_token,
                              'unfollow_non_following': self.cat_token,
                              }

        self.response_bodies = {'follow_for_other': {"message": "Not allowed to follow for another user."},
                                'get_following': {
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "lion's following activities.",
            "type": "Collection",
            "total_items": 2,
            "items": [
                {
                    "@context": "https://www.w3.org/ns/activitystreams",
                    "summary": "lion followed cat",
                    "type": "Follow",
                    "actor": {
                        "type": "https://schema.org/Person",
                        "@id": self.lion_user.user_id,
                        "identifier": self.lion_user.identifier
                    },
                    "object": {
                        "type": "https://schema.org/Person",
                        "@id": self.cat_user.user_id,
                        "identifier": self.cat_user.identifier
                    }
                },
                {
                    "@context": "https://www.w3.org/ns/activitystreams",
                    "summary": "lion followed dog",
                    "type": "Follow",
                    "actor": {
                        "type": "https://schema.org/Person",
                        "@id": self.lion_user.user_id,
                        "identifier": self.lion_user.identifier
                    },
                    "object": {
                        "type": "https://schema.org/Person",
                        "@id": self.dog_user.user_id,
                        "identifier": self.dog_user.identifier
                    }
                },
            ]
        },
            'get_follower': {
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "cat's being followed activities.",
            "type": "Collection",
            "total_items": 1,
            "items": [
                {
                    "@context": "https://www.w3.org/ns/activitystreams",
                    "summary": "lion followed cat",
                    "type": "Follow",
                    "actor": {
                        "type": "https://schema.org/Person",
                        "@id": self.lion_user.user_id,
                        "identifier": self.lion_user.identifier
                    },
                    "object": {
                        "type": "https://schema.org/Person",
                        "@id": self.cat_user.user_id,
                        "identifier": self.cat_user.identifier
                    }
                }
            ]
        },
            'already_followed': {"message": "User already followed."},
            'follow_yourself': {"message": "User cannot follow itself."},
            'follow_non_existing': {"message": "Enter a valid user_id to follow."},
            'unfollow_for_other': {"message": "Not allowed to unfollow for another user."},
            'unfollow_non_following': {"message": "Enter a valid user_id to unfollow."},
        }

    def test_follow_success(self):
        test_type = 'follow_success'
        request_param = self.request_param[test_type]
        request_user_id = self.request_user_id[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/follower"

        request_body = {"user_id": request_user_id}
        response = self.client.post(
            path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Follow.objects.filter(
            follower=request_param, following=request_user_id).exists())

    def test_follow_for_other(self):
        test_type = 'follow_for_other'
        request_param = self.request_param[test_type]
        request_user_id = self.request_user_id[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/follower"

        request_body = {"user_id": request_user_id}
        response = self.client.post(
            path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertFalse(Follow.objects.filter(
            follower=request_param, following=request_user_id).exists())

    def test_already_followed(self):
        test_type = 'already_followed'
        request_param = self.request_param[test_type]
        request_user_id = self.request_user_id[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/follower"

        request_body = {"user_id": request_user_id}
        response = self.client.post(
            path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_follow_yourself(self):
        test_type = 'follow_yourself'
        request_param = self.request_param[test_type]
        request_user_id = self.request_user_id[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/follower"

        request_body = {"user_id": request_user_id}
        response = self.client.post(
            path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_follow_non_existing(self):
        test_type = 'follow_non_existing'
        request_param = self.request_param[test_type]
        request_user_id = self.request_user_id[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/follower"

        request_body = {"user_id": request_user_id}
        response = self.client.post(
            path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_unfollow_success(self):
        test_type = 'unfollow_success'
        request_param = self.request_param[test_type]
        request_user_id = self.request_user_id[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/follower"

        request_body = {"user_id": request_user_id}
        response = self.client.delete(
            path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Follow.objects.filter(
            follower=request_param, following=request_user_id).exists())

    def test_unfollow_for_other(self):
        test_type = 'unfollow_for_other'
        request_param = self.request_param[test_type]
        request_user_id = self.request_user_id[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/follower"

        request_body = {"user_id": request_user_id}
        response = self.client.delete(
            path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_unfollow_non_following(self):
        test_type = 'unfollow_non_following'
        request_param = self.request_param[test_type]
        request_user_id = self.request_user_id[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/follower"

        request_body = {"user_id": request_user_id}
        response = self.client.delete(
            path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_get_follower(self):
        test_type = 'get_follower'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/follower"

        response = self.client.get(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_get_following(self):
        test_type = 'get_following'
        request_param = self.request_param[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/following"

        response = self.client.get(
            path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])
