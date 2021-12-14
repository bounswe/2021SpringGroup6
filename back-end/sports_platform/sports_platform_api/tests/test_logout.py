from django.test import Client, TestCase
from ..models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .test_helper_functions import create_mock_user


class LogoutTest(TestCase):

    def setUp(self):
        self.client = Client()

        lion_info = {'identifier': 'lion',
                     'password': 'roarroar', 'email': 'lion@roar.com'}
        cat_info = {'identifier': 'cat',
                    'password': 'meowmeow', 'email': 'cat@meow.com'}

        self.lion_user = create_mock_user(lion_info)
        self.cat_user = create_mock_user(cat_info)

        self.lion_token, _ = Token.objects.get_or_create(user=self.lion_user)
        self.cat_token, _ = Token.objects.get_or_create(user=self.cat_user)

        authenticate(identifier=self.cat_user.identifier,
                     password=self.cat_user.password)

        self.response_bodies = {'invalid_token': {"message": "Invalid token."},
                                'no_token': {"message": "User not logged in."},
                                'success': {"message": "Successfully logged out."}
                                }

        self.path = '/users/logout'

    def test_invalid_token(self):
        test_type = 'invalid_token'
        response = self.client.post(
            self.path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token invalidtoken'})
        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertEqual(response.status_code, 401)

    def test_no_token(self):
        test_type = 'no_token'
        response = self.client.post(
            self.path, content_type='application/json')
        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertEqual(response.status_code, 401)

    def test_success(self):
        test_type = 'success'
        response = self.client.post(
            self.path, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.cat_token.key}'})
        self.assertEqual(response.data, self.response_bodies[test_type])
        self.assertEqual(response.status_code, 200)
