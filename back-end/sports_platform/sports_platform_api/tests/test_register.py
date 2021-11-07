from django.test import Client, TestCase

class RegisterTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.request_body = {'identifier':'asds', 'email':'berk@boun.com', 'password':'qwerttyty'}

    def test_without_email(self):
        self.request_body.pop('email')
        response = self.client.post('/users',self.request_body)
        self.assertEqual(response.status_code, 400)
    
    def test_without_password(self):
        self.request_body.pop('password')
        response = self.client.post('/users',self.request_body)
        self.assertEqual(response.status_code, 400)
    
    def test_without_identifier(self):
        self.request_body.pop('identifier')
        response = self.client.post('/users',self.request_body)
        self.assertEqual(response.status_code, 400)
    
    def test_success(self):
        response = self.client.post('/users',self.request_body)
        self.assertEqual(response.status_code, 201)
    
    def test_invalid_name(self):
        self.request_body['name']='HATİCE'
        response = self.client.post('/users',self.request_body)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['name'][0],'Only English characters and . are allowed.')
    
    def test_invalid_password(self):
        self.request_body['password']='qwerty'
        response = self.client.post('/users',self.request_body)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),'Password Requirements are not satisfied')