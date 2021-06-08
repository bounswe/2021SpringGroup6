import unittest
from ..views import url_handler_events

class TestEventAPI(unittest.TestCase):

    def setUp(self):
        self.base = "http://127.0.0.1:5000/api/v1.0/events"

    # test for no filter
    def test_no_filter(self):
        url_expected = "http://127.0.0.1:5000/api/v1.0/events"
        url_method = url_handler_events(self.base, None, None, None, None)
        self.assertEqual(url_expected, url_method)
        
    # test for filter by name
    def test_filter_by_name(self):
        url_expected = "http://127.0.0.1:5000/api/v1.0/events?name=street"
        url_method = url_handler_events(self.base, 'street', None, None, None)
        self.assertEqual(url_expected, url_method)

    # test for filter by sport
    def test_filter_by_sport(self):
        url_expected = "http://127.0.0.1:5000/api/v1.0/events?sport=106"
        url_method = url_handler_events(self.base, None, 106, None, None)
        self.assertEqual(url_expected, url_method)

    # test for filter by date_from
    def test_filter_by_date_from(self):
        url_expected = "http://127.0.0.1:5000/api/v1.0/events?date_from=2021-06-08T18:00"
        url_method = url_handler_events(self.base, None, None, '2021-06-08T18:00', None)
        self.assertEqual(url_expected, url_method)

    # test for filter by date_to
    def test_filter_by_date_to(self):
        url_expected = "http://127.0.0.1:5000/api/v1.0/events?date_to=2021-06-09T18:00"
        url_method = url_handler_events(self.base, None, None, None, '2021-06-09T18:00')
        self.assertEqual(url_expected, url_method)
    
    # test for filter by sport and date_from
    def test_filter_by_sport_and_date_from(self):
        url_expected = "http://127.0.0.1:5000/api/v1.0/events?sport=106&date_from=2021-06-08T18:00"
        url_method = url_handler_events(self.base, None, 106, '2021-06-08T18:00', None)
        self.assertEqual(url_expected, url_method)

    # test for filter by date_from and date_to
    def test_filter_by_date_from_to(self):
        url_expected = "http://127.0.0.1:5000/api/v1.0/events?date_from=2021-06-08T18:00&date_to=2021-06-09T18:00"
        url_method = url_handler_events(self.base, None, None, '2021-06-08T18:00', '2021-06-09T18:00')
        self.assertEqual(url_expected, url_method)
    
    # test for filter by name and sport
    def test_filter_by_name_and_sport(self):
        url_expected = "http://127.0.0.1:5000/api/v1.0/events?name=street&sport=106"
        url_method = url_handler_events(self.base, "street", 106, None, None)
        self.assertEqual(url_expected, url_method)


if __name__ == '__main__':
    unittest.main()
