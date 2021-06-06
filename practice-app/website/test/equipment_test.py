import unittest
import requests
from ...main import app
from ..api import equipment

class TestEquipmentAPI(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_equipments_POST(self):
        response = self.app.post('/api/v1.0/equipments', json={
            'name': ''
        })
        json_data = response.get_json()
        self.assertEqual(json_data.status, '200 OK')
        





