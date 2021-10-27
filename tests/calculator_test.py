import unittest
from modules.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculate_1 = Calculator(2, 3, 5)
        self.calculate_2 = Calculator(10, 5, 5)
        self.calculate_3 = Calculator(3, 4, 12)
        self.calculate_4 = Calculator(16, 4, 4)

    def test_calculate_has_first_number(self):
        self.assertEqual(2, self.calculate_1.first_number)

    def test_calculate_has_second_number(self):
        self.assertEqual(3, self.calculate_1.second_number)

    def test_calculate_has_sum(self):
        self.assertEqual(5, self.calculate_1.sum)

    def test_adds_numbers(self):
        self.calculate_1.add_numbers(self.calculate_1.first_number, self.calculate_1.second_number)
        self.assertEqual(5, self.calculate_1.sum)

    def test_subtracts_numbers(self):
        self.calculate_2.subtract_numbers(self.calculate_2.first_number, self.calculate_2.second_number)
        self.assertEqual(5, self.calculate_2.sum)

    def test_multiplies_numbers(self):
        self.calculate_3.multiply_numbers(self.calculate_3.first_number, self.calculate_3.second_number)
        self.assertEqual(12, self.calculate_3.sum)

    def test_divides_numbers(self):
        self.calculate_4.divide_numbers(self.calculate_4.first_number, self.calculate_4.second_number)
        self.assertEqual(4, self.calculate_4.sum)