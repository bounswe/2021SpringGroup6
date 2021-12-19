from django.test import Client, TestCase
from ..models import Block
from rest_framework.authtoken.models import Token
from .test_helper_functions import create_mock_user
from ..serializers.user_serializer import UserSerializer

class SearchUserTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.maxDiff = None
        lion_info = {'identifier': 'lion', 'name':'lion',
                     'password': 'roarroar', 'email': 'lion@roar.com'}
        cat_info = {'identifier': 'cat', 'name':'cat',
                    'password': 'meowmeow', 'email': 'cat@meow.com'}

        self.lion_user = create_mock_user(lion_info)
        self.cat_user = create_mock_user(cat_info)

        self.lion_token, _ = Token.objects.get_or_create(user=self.lion_user)

        self.request_bodies = {'no_filter': {},
                               'multiple_filters': {'name': 'abc','identifier':'cdf'},
                               'name': {'name':'ca'},
                               'identifier': {'identifier': 'cat'},
                               'block':{'name':'cat'}
                               }

        user_res = UserSerializer(self.cat_user).data
        user_res['@context'] = 'https://schema.org/Person'
        user_res['@id'] = self.cat_user.user_id
        user_res['@type'] = 'Person'
        user_res['knowsAbout'] = []
        success_response =  {'@context':"https://www.w3.org/ns/activitystreams", 'type':'Collection',
                          'total_items':1,'items':[user_res]}
        self.response_bodies = {'no_filter': {"message": {"nameContains": "Exactly 1 filter should be provided. Options are name, familyName and identifier"}},
                                'multiple_filters': {"message": {"nameContains": "Exactly 1 filter should be provided. Options are name, familyName and identifier"}},
                                'name': success_response,
                                'identifier': success_response,
                                'block':{'@context':"https://www.w3.org/ns/activitystreams", 'type':'Collection',
                                'total_items':0,'items':[]}
                                }

        self.path = '/users/searches'

    def test_no_filter(self):
        test_type = 'no_filter'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])
    
    def test_multiple_filtersr(self):
        test_type = 'multiple_filters'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])
    
    
    def test_filter_name(self):
        test_type = 'name'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])
    
    def test_filter_identifier(self):
        test_type = 'identifier'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])
    
    def test_block(self):
        test_type = 'block'
        Block.objects.create(blocker=self.cat_user, blocked=self.lion_user)
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body, content_type='application/json', **{'HTTP_AUTHORIZATION': f'Token {self.lion_token}'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.response_bodies[test_type])
    