from django.test import Client, TestCase
from ..models import Block
from rest_framework.authtoken.models import Token
from .test_helper_functions import create_mock_user

class BlockTest(TestCase):

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

        self.request_param = {'block_success': self.cat_user.user_id,
                              'block_for_other': self.dog_user.user_id,
                              'already_blocked': self.lion_user.user_id,
                              'block_yourself': self.cat_user.user_id,
                              'block_non_existing': self.cat_user.user_id
                              }

        self.request_user_id = {'block_success': self.dog_user.user_id,
                                'block_for_other': self.lion_user.user_id,
                                'already_blocked': self.dog_user.user_id,
                                'block_yourself': self.cat_user.user_id,
                                'block_non_existing': 13
                                }

        self.request_token = {'block_success': self.cat_token,
                              'block_for_other': self.cat_token,
                              'already_blocked': self.lion_token,
                              'block_yourself': self.cat_token,
                              'block_non_existing': self.cat_token
                              }                              

        self.response_bodies = {'block_for_other': {"message": "Not allowed to block for another user."},
            'already_blocked': {"message": "User already blocked."},
            'block_yourself': {"message": "User cannot block herself."},
            'block_non_existing': {"message": "Enter a valid user_id to block."}
        }

    def test_block_success(self):
        test_type = 'block_success'
        request_param = self.request_param[test_type]
        request_user_id = self.request_user_id[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/blocked"

        request_body = {"user_id": request_user_id}
        response = self.client.post(
            path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Block.objects.filter(
            blocker=request_param, blocked=request_user_id).exists())

    def test_block_for_other(self):
        test_type = 'block_for_other'
        request_param = self.request_param[test_type]
        request_user_id = self.request_user_id[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/blocked"

        request_body = {"user_id": request_user_id}
        response = self.client.post(
            path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertFalse(Block.objects.filter(
            blocker=request_param, blocked=request_user_id).exists())

    def test_already_blocked(self):
        test_type = 'already_blocked'
        request_param = self.request_param[test_type]
        request_user_id = self.request_user_id[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/blocked"

        request_body = {"user_id": request_user_id}
        response = self.client.post(
            path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_block_yourself(self):
        test_type = 'block_yourself'
        request_param = self.request_param[test_type]
        request_user_id = self.request_user_id[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/blocked"

        request_body = {"user_id": request_user_id}
        response = self.client.post(
            path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_block_non_existing(self):
        test_type = 'block_non_existing'
        request_param = self.request_param[test_type]
        request_user_id = self.request_user_id[test_type]
        token = self.request_token[test_type]

        path = "/users/" + str(request_param) + "/blocked"

        request_body = {"user_id": request_user_id}
        response = self.client.post(
            path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])