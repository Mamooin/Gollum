import unittest
from rectangle import area, perimeter

class TestRectangleFunctions(unittest.TestCase):

    def test_area(self):
        # Проверка правильности вычисления площади прямоугольника
        self.assertEqual(area(3, 4), 12)
        self.assertEqual(area(5, 7), 35)
        self.assertEqual(area(0, 10), 0)

    def test_perimeter(self):
        # Проверка правильности вычисления периметра прямоугольника
        self.assertEqual(perimeter(3, 4), 14)
        self.assertEqual(perimeter(5, 7), 24)
        self.assertEqual(perimeter(0, 10), 20)

    def test_negative_values(self):
        # Проверка работы с отрицательными значениями
        self.assertEqual(area(-2, 6), 0)  # Площадь не может быть отрицательной
        self.assertEqual(perimeter(-2, 6), 8)  # Периметр = 2 * (a + b) = 2 * (4) = 8
