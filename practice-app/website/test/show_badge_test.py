import unittest
from ..api.badge import get_cat_pictures

class Test_Cat_Pictures(unittest.TestCase):
    def setUp(self):
        self.badges = ["Badge1", "Badge2", "Badge3"]
        self.empty = []
    
    def test_pictures_length(self):
        pictures_result = get_cat_pictures(self.badges)
        self.assertEqual(len(self.badges), len(pictures_result))
        
    def test_empty(self):
        empty_result = get_cat_pictures(self.empty)
        self.assertEqual(len(self.empty), len(empty_result))  

    def test_pictures_type(self):
        pictures_result = get_cat_pictures(self.badges)
        self.assertEqual(type(""), type(pictures_result[0]))
        self.assertEqual(type(""), type(pictures_result[1]))
        self.assertEqual(type(""), type(pictures_result[2]))