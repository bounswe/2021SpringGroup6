import unittest
import requests, json
from ..api.event import check_comment_has_text

class TestEventAPI(unittest.TestCase):

    # given an empty comment, it returns false
    def test_comment_has_test(self):
        comment = ""
        result = check_comment_has_text(comment)
        self.assertEqual(result, False)
