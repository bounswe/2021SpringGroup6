import unittest
from ..api.badge import extract_point, prepare_badge
from ..models import Badge

class TestBadgeAPI(unittest.TestCase):

    def setUp(self):
         self.data = {'name':'mvp', 'symbol':'trialpicture.com'}
         self.bitcoin_price = 32.4523478

    def test_badges(self):
        expected = Badge(name=self.data['name'], symbol=self.data['symbol'])
        badge = prepare_badge(self.data)

        self.assertEqual(expected.name, badge.name)
        self.assertEqual(expected.symbol, badge.symbol)
    
    def test_badge_point(self):
        expected = extract_point(self.bitcoin_price)
        self.assertEqual(expected,'3') # 3 is the 4th digit after decimal point