from django.test import Client, TestCase
from rest_framework.authtoken.models import Token
from ..models import User
from ..serializers.user_serializer import UserSerializer
from .test_helper_functions import create_mock_user


class GetUserTest(TestCase):
    def setUp(self):
        self.client = Client()
        info_retriever = {'identifier':'lion', 'password': 'roarroar', 'email': 'lion@roar.com'}
        self.getting_user = create_mock_user(info_retriever)
        self.getting_user_token, _ = Token.objects.get_or_create(user=self.getting_user)

        info_retrieved = {'identifier':'lion1', 'password': 'roarroar', 'email': 'lion1@roar.com'}
        retrieved_user = create_mock_user(info_retrieved)
        self.serialzed_retrieved_user = UserSerializer(retrieved_user).data
        self.serialzed_retrieved_user.pop('last_login')
        self.serialzed_retrieved_user['@context'] = 'https://schema.org/Person'
        self.serialzed_retrieved_user['@id'] = self.serialzed_retrieved_user['user_id']
        self.serialzed_retrieved_user['knowsAbout'] = []

        self.header = {'HTTP_AUTHORIZATION': f'Token {self.getting_user_token}'}
        self.path = f'/users/{self.serialzed_retrieved_user["user_id"]}'
        self.invalid_user_path = f'/users/{100}'

    def test_user_not_exist(self):
        response = self.client.get(self.invalid_user_path,**self.header)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['message'],'User id does not exist')

    def test_success(self):
        response = self.client.get(self.path,**self.header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.serialzed_retrieved_user)