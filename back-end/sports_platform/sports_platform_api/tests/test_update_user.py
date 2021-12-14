from django.test import Client, TestCase
from rest_framework.authtoken.models import Token
from .test_helper_functions import create_mock_user


class UpdateUserTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = create_mock_user({'identifier':'lion', 'password': 'roarroar', 'email': 'lion@roar.com'})
        self.user_token, _ = Token.objects.get_or_create(user=self.user)
        self.update_info = {'name':'berk','familyName':'atil'}
        self.header = {'HTTP_AUTHORIZATION': f'Token {self.user_token}'}
        self.path = f'/users/{self.user.user_id}'
        self.invalid_user_path = f'/users/{100}'

    def test_not_authorized(self):
        response = self.client.put(self.invalid_user_path,self.update_info)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['message'],'Login required.')

    def test_success(self):
        response = self.client.put(self.path,content_type='application/json', data=self.update_info, **self.header)
        self.assertEqual(response.status_code, 200)