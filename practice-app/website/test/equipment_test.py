import unittest
from ..api.equipment import get_price
from ..models import Equipment

class TestEventAPI(unittest.TestCase):

    def test_price(self):
        """
            Price a string which has value of 0.0
        """
        price_value = get_price()

        self.assertEqual(price_value, "0.0")
