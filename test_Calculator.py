import unittest

from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        test_data = CsvReader("Unit Test Subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_add_method_calculator(self):
        test_data_add = CsvReader('Unit Test Addition.csv').data
        for row in test_data_add:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_multiply_method_calculator(self):
        test_data_multiply = CsvReader('Unit Test Multiplication.csv').data
        for row in test_data_multiply:
            self.assertEqual(self.calculator.mul(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_divide_method_calculator(self):
        test_data_divide = CsvReader('Unit Test Division.csv').data
        for row in test_data_divide:
            self.assertEqual(round(self.calculator.division(row['Value 1'], row['Value 2']), 2),
                             round(float(row['Result']), 2))
            self.assertEqual(round(self.calculator.result, 2), round(float(row['Result']), 2))

    def test_square_method_calculator(self):
        test_data_square = CsvReader('Unit Test Square.csv').data
        for row in test_data_square:
            self.assertEqual(self.calculator.sq(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_square_root_method_calculator(self):
        test_data_square_root = CsvReader('Unit Test Square Root.csv').data
        for row in test_data_square_root:
            self.assertEqual(round(self.calculator.sqr(row['Value 1']), 2), round(float(row['Result']), 2))
            self.assertEqual(round(self.calculator.result, 2), round(float(row['Result']), 2))

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
