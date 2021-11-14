from django.test import Client, TestCase
from ..models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .test_helper_functions import create_mock_user
from django.core import mail

class RecoverTest(TestCase):

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

        self.request_bodies = {'wrong_email': {'email': 'lion3@roar.com'},
                               'no_email': {},
                               'success': {'email': 'lion@roar.com'},
                               'already_logged_in': {'email': 'cat@meow.com'},
                               }

        self.response_bodies = {'wrong_email': {"message": "If email provided is correct, a reset password is sent, please check spam."},
                                'no_email': {"message": {"email": ["This field is required."]}},
                                'success': {"message": "If email provided is correct, a reset password is sent, please check spam."},
                                'already_logged_in': {"message": "Already logged in use change password on settings instead."},
                                }

        self.path = '/users/recover'

    def test_wrong_email(self):
        test_type = 'wrong_email'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body)

        self.assertEqual(len(mail.outbox), 0)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_no_email(self):
        test_type = 'no_email'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body)

        self.assertEqual(len(mail.outbox), 0)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_already_logged_in(self):
        test_type = 'already_logged_in'
        request_body = self.request_bodies[test_type]
        response = self.client.post(
            self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.cat_token.key}'})

        self.assertEqual(len(mail.outbox), 0)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, self.response_bodies[test_type])
    
    def test_success(self):
        test_type = 'success'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject,
                         'New Password for your Squad Game Account')
        self.assertIn(
            f"new password for the account with username {self.lion_user.identifier} is", mail.outbox[0].body)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])

        authenticed = authenticate(identifier=self.lion_user.identifier,
                     password=self.lion_user.password)

        self.assertIsNone(authenticed)

        new_pass = mail.outbox[0].body.split(",")[0][-15:]

        authenticed_new = authenticate(identifier=self.lion_user.identifier,
                                       password=new_pass)

        self.assertEqual(authenticed_new.user_id, self.lion_user.user_id)
