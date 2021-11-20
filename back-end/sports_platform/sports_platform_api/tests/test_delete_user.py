from django.test import Client, TestCase
from .test_helper_functions import create_mock_user
from rest_framework.authtoken.models import Token

class DeleteUserTest(TestCase):
    def setUp(self):
        self.client = Client()
        lion_info = {'identifier': 'lion',
                     'password': 'roarroar', 'email': 'lion@roar.com'}

        self.lion_user = create_mock_user(lion_info)

        self.lion_token, _ = Token.objects.get_or_create(user=self.lion_user)
        self.header = {'HTTP_AUTHORIZATION': f'Token {self.lion_token}'}
        self.path = f'/users/{self.lion_user.user_id}'

    def test_success(self):
        response = self.client.delete(self.path, **self.header)
        self.assertEqual(response.status_code, 200)
    
    def test_not_authorized(self):
        response = self.client.delete(self.path)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['message'],'User not logged in.')