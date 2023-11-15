import unittest
from triangle import area, perimeter
class TestTriangleFunctions(unittest.TestCase):

    def test_area(self):
        # Проверка правильности вычисления площади треугольника
        self.assertEqual(area(2, 3), 3)  # Площадь треугольника с основанием 2 и высотой 3
        self.assertEqual(area(4, 5), 10)  # Площадь треугольника с основанием 4 и высотой 5
        self.assertEqual(area(0, 7), 0)  # Площадь треугольника с нулевой основой

    def test_perimeter(self):
        # Проверка правильности вычисления периметра треугольника
        self.assertEqual(perimeter(2, 3, 4), 9)  # Периметр треугольника со сторонами 2, 3 и 4
        self.assertEqual(perimeter(5, 12, 13), 30)  # Периметр треугольника со сторонами 5, 12 и 13
        self.assertEqual(perimeter(1, 1, 1), 3)  # Периметр треугольника со сторонами 1, 1 и 1

    def test_negative_side(self):
        # Проверка работы с отрицательными сторонами
        self.assertEqual(area(-2, 3), 0)  # Площадь треугольника не может быть отрицательной
        self.assertEqual(perimeter(-2, 3, 4), 0)  # Периметр треугольника не может быть отрицательным
