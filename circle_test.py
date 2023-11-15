import unittest
import math
from circle import area, perimeter
class TestCircleFunctions(unittest.TestCase):

    def test_area(self):
        # �������� ������������ ���������� ������� �����
        self.assertAlmostEqual(area(1), math.pi)  # ������� ����� � �������� 1
        self.assertAlmostEqual(area(2), 4 * math.pi)  # ������� ����� � �������� 2
        self.assertAlmostEqual(area(0), 0)  # ������� ����� � �������� 0

    def test_perimeter(self):
        # �������� ������������ ���������� ����� ����������
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)  # ����� ���������� � �������� 1
        self.assertAlmostEqual(perimeter(3), 6 * math.pi)  # ����� ���������� � �������� 3
        self.assertAlmostEqual(perimeter(0), 0)  # ����� ���������� � �������� 0

    def test_negative_radius(self):
        # �������� ������ � ������������� ��������
        self.assertAlmostEqual(area(-2), 0)  # ������� ����� �� ����� ���� �������������
        self.assertAlmostEqual(perimeter(-2), 0)  # ����� ���������� �� ����� ���� �������������

