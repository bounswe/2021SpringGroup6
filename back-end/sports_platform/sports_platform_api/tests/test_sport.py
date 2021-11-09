from django.test import Client, TestCase
from rest_framework.authtoken.models import Token
from .test_helper_functions import create_mock_user
from ..models import Sport

class GetSportTest(TestCase):
    def setUp(self):
        self.client = Client()
        info = {'identifier':'lion', 'password': 'roarroar', 'email': 'lion@roar.com'}
        self.user = create_mock_user(info)
        self.user_token, _ = Token.objects.get_or_create(user=self.user)

        self.header = {'HTTP_AUTHORIZATION': f'Token {self.user_token}'}
        self.path = '/sports'
        Sport.objects.create(name="soccer")
        Sport.objects.create(name="hockey")
        self.sports = { "sport_names": ["soccer", "hockey"]}

    def test_unauthorized(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['message'], 'User is not logged in, first you need to login')

    def test_success(self):
        response = self.client.get(self.path,**self.header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.sports)