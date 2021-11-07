from django.test import Client, TestCase

class RegisterTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.request_body = {'identifier':'asds', 'email':'berk@boun.com', 'password':'qwerttyty'}

        self.path = '/users'

    def test_without_email(self):
        self.request_body.pop('email')
        response = self.client.post(self.path,self.request_body)
        self.assertEqual(response.status_code, 400)
    
    def test_without_password(self):
        self.request_body.pop('password')
        response = self.client.post(self.path,self.request_body)
        self.assertEqual(response.status_code, 400)
    
    def test_without_identifier(self):
        self.request_body.pop('identifier')
        response = self.client.post(self.path,self.request_body)
        self.assertEqual(response.status_code, 400)
    
    def test_success(self):
        response = self.client.post(self.path,self.request_body)
        self.assertEqual(response.status_code, 201)
    
    def test_invalid_name(self):
        self.request_body['name']='HATİCE'
        response = self.client.post(self.path,self.request_body)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['message']['name'][0],'Only English characters and . are allowed. Cannot start or end with .')
    
    def test_invalid_password(self):
        self.request_body['password']='qwerty'
        response = self.client.post(self.path,self.request_body)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['message']['password'], ['Ensure this field has at least 8 characters.'])