from django.test import Client, TestCase
from ..models import Block
from rest_framework.authtoken.models import Token
from .test_helper_functions import create_mock_user

class UnBlockTest(TestCase):

    def setUp(self):
        self.client = Client()

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

        Block.objects.create(blocker=self.lion_user, blocked=self.cat_user)
        Block.objects.create(blocker=self.lion_user, blocked=self.dog_user)

        self.request_param = {'unblock_success': self.lion_user.user_id,
                              'unblock_for_other': self.lion_user.user_id,
                              'unblock_non_blocked': self.cat_user.user_id
                              }

        self.request_user_id = {'unblock_success': self.cat_user.user_id,
                                'unblock_for_other': self.dog_user.user_id,
                                'unblock_non_blocked': self.dog_user.user_id
                                }

        self.request_token = {'unblock_success': self.lion_token,
                              'unblock_for_other': self.cat_token,
                              'unblock_non_blocked': self.cat_token
                              }                              

        self.response_bodies = {'unblock_for_other': {"message": "Not allowed to unblock for another user."},
            'unblock_non_blocked': {"message": "Enter a valid user_id to unblock."}
        }

    def test_unblock_success(self):
        test_type = 'unblock_success'
        request_param = self.request_param[test_type]
        request_user_id = self.request_user_id[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/blocked"

        request_body = {"user_id": request_user_id}
        response = self.client.delete(
            path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Block.objects.filter(
            blocker=request_param, blocked=request_user_id).exists())

    def test_unblock_for_other(self):
        test_type = 'unblock_for_other'
        request_param = self.request_param[test_type]
        request_user_id = self.request_user_id[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/blocked"

        request_body = {"user_id": request_user_id}
        response = self.client.delete(
            path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_unblock_non_blocked(self):
        test_type = 'unblock_non_blocked'
        request_param = self.request_param[test_type]
        request_user_id = self.request_user_id[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/blocked"

        request_body = {"user_id": request_user_id}
        response = self.client.delete(
            path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])