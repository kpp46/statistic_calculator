import ast
import random
import unittest

import numpy as np
from numpy.random import randint
from numpy.random import seed

from Confidence_interval import confidence_interval_bottom
from Confidence_interval import result_confidence_interval_bottom
from CsvReader import CsvReader
from ItemsWithSeed import items_with_seed
from ItemsWoutSeed import items_without_seed
from Margin_Error import margin_error2
from Margin_Error import result_margin_error2
from NListWithSeed import generator_int_and_float
from RandomItem import random_item
from RandomNumberWithSeed import random_integer, random_float
from RandomlySelectSame import randomly_same
from Sample_random_Sampling import population
from Statistics import Statistics
from TestSize import result_testSize
from TestSize import testSize
from TestWithoutStandDevi import TestWithoutStandDevi
from TestWithoutStandDevi import result_withoutStandDevi


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = randint(0, 10, 20)
        self.statistics = Statistics()
        self.x = 1
        self.sample = generator_int_and_float(10, 35)

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        test_data_mean = CsvReader("descriptive_stats.csv").data
        for row in test_data_mean:
            input_data = ast.literal_eval(row['input'])  # This converts string representation of list into list type
            self.assertEqual(round(self.statistics.mean(input_data), 2), round(float(row['mean']), 2))
            self.assertEqual(round(self.statistics.result, 2), round(float(row['mean']), 2))

    def test_median_statistics(self):
        test_data_median = CsvReader("descriptive_stats.csv").data
        for row in test_data_median:
            input_data = ast.literal_eval(row['input'])
            self.assertEqual(round(self.statistics.median(input_data), 2), round(float(row['median']), 2))
            self.assertEqual(round(self.statistics.result, 2), round(float(row['median']), 2))

    def test_mode_statistics(self):
        test_data_mode = CsvReader("descriptive_stats.csv").data
        for row in test_data_mode:
            input_data = ast.literal_eval(row['input'])
            mode_data = ast.literal_eval(row['mode'])
            self.assertEqual(self.statistics.mode(input_data), mode_data)
            self.assertEqual(self.statistics.result, mode_data)

    def test_variance_statistics(self):
        test_data_variance = CsvReader("descriptive_stats.csv").data
        for row in test_data_variance:
            input_data = ast.literal_eval(row['input'])
            self.assertEqual(round(self.statistics.variance(input_data), 2), round(float(row['variance']), 2))
            self.assertEqual(round(self.statistics.result, 2), round(float(row['variance']), 2))

    def test_stddev_statistics(self):
        test_data_stddev = CsvReader("descriptive_stats.csv").data
        for row in test_data_stddev:
            input_data = ast.literal_eval(row['input'])
            self.assertEqual(round(self.statistics.stddev(input_data), 2), round(float(row['standard_deviation']), 2))
            self.assertEqual(round(self.statistics.result, 2), round(float(row['standard_deviation']), 2))

    def test_items_with_seed(self):
        nlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        random.seed(5)
        result_number_list = random.sample(nlist, 5)
        self.assertEqual(len(items_with_seed(5)), len(result_number_list))

    def test_items_Wout_seed(self):
        nlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result_number_list = random.sample(nlist, 5)
        self.assertEqual(len(items_without_seed(5)), len(result_number_list))
        self.assertNotEqual(items_without_seed(5), result_number_list)

    def test_randomly_same(self):
        nlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        random.seed(5)
        number_list = random.sample(nlist, 1)
        self.assertEqual(randomly_same(1), number_list)

    def random_item(self):
        nList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result_numbered_list = random.sample(nList, 5)
        self.assertEqual(len(random_item(5)), len(result_numbered_list))

    def random_integer(self):
        nlist = (range(1, 10))
        random.seed(5)
        result_number_list = random.sample(nlist, 5)
        self.assertEqual(len(random_integer(5)), len(result_number_list))

    def random_float(self):
        nlist = (np.arange(1.0, 10.0))
        random.seed(5)
        result_ran_float = random.uniform(nlist, 5)
        self.assertEqual(len(random_float(5)), len(result_ran_float))
        result_number_list = random.sample(nlist, 5)
        self.assertEqual(randomly_same(5), result_number_list)

    def test_confidence_interval_bottom(self):
        self.assertEqual(round(confidence_interval_bottom(90, self.sample), 1),
                         round(result_confidence_interval_bottom(90, self.sample), 1))

    def test_Sample_random_Sampling(self):
        self.assertNotEqual(population(10, 30), generator_int_and_float(10, 30))

    def test_margin_error(self):
        self.assertEqual(margin_error2(99.9, self.sample), result_margin_error2(99.9, self.sample))

    def test__Size(self):
        self.assertEqual(testSize(50, 95, 0.05), result_testSize(50, 95, 0.05))

    def test_withoutStandDevi(self):
        self.assertEqual(TestWithoutStandDevi(41, 59, 0.06), result_withoutStandDevi(41, 59, 0.06))


if __name__ == '__main__':
    unittest.main()
