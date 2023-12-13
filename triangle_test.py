import unittest
from triangle import area, perimeter
class TestTriangleFunctions(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(2, 3), 3)
        self.assertEqual(area(4, 5), 10)
        self.assertEqual(area(0, 7), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 3, 4), 9)
        self.assertEqual(perimeter(5, 12, 13), 30)
        self.assertEqual(perimeter(1, 1, 1), 3)

    def test_negative_side(self):
        self.assertEqual(area(-2, 3), 0)
        self.assertEqual(perimeter(-2, 3, 4), 0)
