import unittest
from ..api.event import query_handler_events

class TestEventAPI(unittest.TestCase):

    # test for no filter
    def test_no_filter(self):
        query_expected = "SELECT * FROM Event;"
        query_method = query_handler_events(None, None, None, None)
        self.assertEqual(query_expected, query_method)
        
    # test for filter by name
    def test_filter_by_name(self):
        query_expected = "SELECT * FROM Event WHERE name LIKE '%street%';"
        query_method = query_handler_events("street", None, None, None)
        self.assertEqual(query_expected, query_method)

    # test for filter by sport
    def test_filter_by_sport(self):
        query_expected = "SELECT * FROM Event WHERE sport = 106;"
        query_method = query_handler_events(None, 106, None, None)
        self.assertEqual(query_expected, query_method)

    # test for filter by date_from
    def test_filter_by_date_from(self):
        query_expected = "SELECT * FROM Event WHERE date >= '2021-06-08T18:00';"
        query_method = query_handler_events(None, None, '2021-06-08T18:00', None)
        self.assertEqual(query_expected, query_method)

    # test for filter by date_to
    def test_filter_by_date_to(self):
        query_expected = "SELECT * FROM Event WHERE date <= '2021-06-09T18:00';"
        query_method = query_handler_events(None, None, None, '2021-06-09T18:00')
        self.assertEqual(query_expected, query_method)
    
    # test for filter by sport and date_from
    def test_filter_by_sport_and_date_from(self):
        query_expected = "SELECT * FROM Event WHERE sport = 106 AND date >= '2021-06-08T18:00';"
        query_method = query_handler_events(None, 106, '2021-06-08T18:00', None)
        self.assertEqual(query_expected, query_method)

    # test for filter by date_from and date_to
    def test_filter_by_date_from_to(self):
        query_expected = "SELECT * FROM Event WHERE date >= '2021-06-08T18:00' AND date <= '2021-06-09T18:00';"
        query_method = query_handler_events(None, None, '2021-06-08T18:00', '2021-06-09T18:00')
        self.assertEqual(query_expected, query_method)
    
    # test for filter by name and sport
    def test_filter_by_name_and_sport(self):
        query_expected = "SELECT * FROM Event WHERE name LIKE '%street%' AND sport = 106;"
        query_method = query_handler_events("street", 106, None, None)
        self.assertEqual(query_expected, query_method)

if __name__ == '__main__':
    unittest.main()
