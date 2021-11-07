from django.test import Client, TestCase
from ..models import User

class LoginTest(TestCase):

    def setUp(self):
        self.client = Client()

        User.objects.create_user(identifier="lion", password="roarroar", email="lion@roar.com")

        self.request_bodies = {'no_identifier':{'password':'qwerttyty'},
        'no_password':{'identifier':'asds'},
        'short_password':{'identifier':'asds', 'password':'qwer'},
        'password_with_special':{'identifier':'asds', 'password':'qwer/ttyty'},
        'identifier_with_special':{'identifier':'as/ds', 'password':'qwerttyty'},
        'identifier_starts_with_dot':{'identifier':'.asds', 'password':'qwerttyty'},
        'short_password_identifier_with_special':{'identifier':'as-ds', 'password':'qwe'},
        'success': {'identifier':'lion', 'password':'roarroar'},
        'wrong_credentials': {'identifier':'notlion', 'password':'roarroar'}
        }

        self.response_bodies = {'no_identifier':{"message": {"identifier": ["This field is required."]}},
        'no_password':{"message": {"password": ["This field is required."]}},
        'short_password':{"message": {"password": ["Ensure this field has at least 8 characters."]}},
        'password_with_special':{"message": {"password": ["Only English characters, numbers, * and . are allowed."]}},
        'identifier_with_special':{"message": {"identifier": ["Only English characters, numbers and . are allowed. Cannot start or end with ."]}},
        'identifier_starts_with_dot':{"message": {"identifier": ["Only English characters, numbers and . are allowed. Cannot start or end with ."]}},
        'short_password_identifier_with_special':{"message": {"identifier": ["Only English characters, numbers and . are allowed. Cannot start or end with ."], "password": ["Ensure this field has at least 8 characters."]}},
        'wrong_credentials':{"message": "Check credentials."},
        }

        self.path = '/users/login'
        

    def test_no_identifier(self):
        test_type = 'no_identifier'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_no_password(self):
        test_type = 'no_password'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_short_password(self):
        test_type = 'short_password'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_password_with_special(self):
        test_type = 'password_with_special'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_identifier_with_special(self):
        test_type = 'identifier_with_special'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_identifier_starts_with_dot(self):
        test_type = 'identifier_starts_with_dot'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_short_password_identifier_with_special(self):
        test_type = 'short_password_identifier_with_special'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.response_bodies[test_type])

    def test_success(self):
        test_type = 'success'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body)
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_wrong_credentials(self):
        test_type = 'wrong_credentials'
        request_body = self.request_bodies[test_type]
        response = self.client.post(self.path, request_body)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data, self.response_bodies[test_type])