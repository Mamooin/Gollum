import unittest
from square import area, perimeter
class TestSquareFunctions(unittest.TestCase):

    def test_area(self):
        # ѕроверка правильности вычислени€ площади квадрата
        self.assertEqual(area(2), 4)  # ѕлощадь квадрата со стороной 2
        self.assertEqual(area(3), 9)  # ѕлощадь квадрата со стороной 3
        self.assertEqual(area(0), 0)  # ѕлощадь квадрата со стороной 0

    def test_perimeter(self):
        # ѕроверка правильности вычислени€ периметра квадрата
        self.assertEqual(perimeter(2), 8)  # ѕериметр квадрата со стороной 2
        self.assertEqual(perimeter(4), 16)  # ѕериметр квадрата со стороной 4
        self.assertEqual(perimeter(0), 0)  # ѕериметр квадрата со стороной 0

    def test_negative_side(self):
        # ѕроверка работы с отрицательной стороной
        self.assertEqual(area(-2), 0)  # ѕлощадь квадрата не может быть отрицательной
        self.assertEqual(perimeter(-2), 0)  # ѕериметр квадрата не может быть отрицательным

