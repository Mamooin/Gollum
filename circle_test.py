import unittest
import math
from circle import area, perimeter
class TestCircleFunctions(unittest.TestCase):

    def test_area(self):
        # Проверка правильности вычисления площади круга
        self.assertAlmostEqual(area(1), math.pi)  # Площадь круга с радиусом 1
        self.assertAlmostEqual(area(2), 4 * math.pi)  # Площадь круга с радиусом 2
        self.assertAlmostEqual(area(0), 0)  # Площадь круга с радиусом 0

    def test_perimeter(self):
        # Проверка правильности вычисления длины окружности
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)  # Длина окружности с радиусом 1
        self.assertAlmostEqual(perimeter(3), 6 * math.pi)  # Длина окружности с радиусом 3
        self.assertAlmostEqual(perimeter(0), 0)  # Длина окружности с радиусом 0

    def test_negative_radius(self):
        # Проверка работы с отрицательным радиусом
        self.assertAlmostEqual(area(-2), 0)  # Площадь круга не может быть отрицательной
        self.assertAlmostEqual(perimeter(-2), 0)  # Длина окружности не может быть отрицательной

