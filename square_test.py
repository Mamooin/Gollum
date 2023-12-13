import unittest
from square import area, perimeter
class TestSquareFunctions(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(2), 4)  
        self.assertEqual(area(3), 9)
        self.assertEqual(area(0), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(2), 8) 
        self.assertEqual(perimeter(4), 16) 
        self.assertEqual(perimeter(0), 0)

    def test_negative_side(self):
        self.assertEqual(area(-2), 0)
        self.assertEqual(perimeter(-2), 0)

