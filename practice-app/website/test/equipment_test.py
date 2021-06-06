import unittest
import requests, json

class TestEquipmentAPI(unittest.TestCase):

    def setUp(self):
        self.req = "http://127.0.0.1:5000/api/v1.0/equipments"
        self.headers = {'Content-type': 'application/json'}

    def test_equipment_POST(self):

        # Equipment named Ball
        Equipment ={
            'name': 'Ball'
        }
        response = requests.post(self.req, data=json.dumps(Equipment), headers=self.headers)
        self.assertEqual(response.status_code, 201)

    def test_equipment_POST_empty_name(self):

        # Name field is missing
        Equipment ={
            'name': ''
        }

        response = requests.post(self.req, data=json.dumps(Equipment), headers=self.headers)
        self.assertEqual(response.status_code, 201)