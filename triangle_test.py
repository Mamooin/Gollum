import unittest
from triangle import area, perimeter
class TestTriangleFunctions(unittest.TestCase):

    def test_area(self):
        # �������� ������������ ���������� ������� ������������
        self.assertEqual(area(2, 3), 3)  # ������� ������������ � ���������� 2 � ������� 3
        self.assertEqual(area(4, 5), 10)  # ������� ������������ � ���������� 4 � ������� 5
        self.assertEqual(area(0, 7), 0)  # ������� ������������ � ������� �������

    def test_perimeter(self):
        # �������� ������������ ���������� ��������� ������������
        self.assertEqual(perimeter(2, 3, 4), 9)  # �������� ������������ �� ��������� 2, 3 � 4
        self.assertEqual(perimeter(5, 12, 13), 30)  # �������� ������������ �� ��������� 5, 12 � 13
        self.assertEqual(perimeter(1, 1, 1), 3)  # �������� ������������ �� ��������� 1, 1 � 1

    def test_negative_side(self):
        # �������� ������ � �������������� ���������
        self.assertEqual(area(-2, 3), 0)  # ������� ������������ �� ����� ���� �������������
        self.assertEqual(perimeter(-2, 3, 4), 0)  # �������� ������������ �� ����� ���� �������������
