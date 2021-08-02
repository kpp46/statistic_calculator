from Zscore import zscore

from Calculator import Calculator
from Confidence_interval import confidence_interval_bottom
from ItemsWithSeed import items_with_seed
from ItemsWoutSeed import items_without_seed
from Margin_Error import margin_error2
from Mean import mean
from Median import median
from Mode import mode
from NListWithSeed import generator_int_and_float
from RandomItem import random_item
from RandomNumberWithSeed import random_integer
from RandomNumberWoutSeed import random_integer
from RandomlySelectSame import randomly_same
from Sample_random_Sampling import population
from Standard_Deviation import stddev
from TestSize import testSize
from TestWithoutStandDevi import TestWithoutStandDevi
from Variance import variance


class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def stddev(self, data):
        self.result = stddev(data)
        return self.result

    def zscore(self, data, x):
        self.result = zscore(data, x)
        return self.result

    def random_integer(self, data, x):
        self.result = random_integer(data, x)
        return self.result

    def items_without_seed(self, data, x):
        self.result = items_without_seed(data, x)
        return self.result

    def items_with_seed(self, data, x):
        self.result = items_with_seed(data, x)
        return self.result

    def generator_int_and_float(self, data, x):
        self.result = generator_int_and_float(data, x)
        return self.result

    def random_item(self, data, x):
        self.result = random_item(data, x)
        return self.result

    def randomly_same(self, data, x):
        self.result = randomly_same(data, x)
        return self.result

    def me(self, probability, data):
        self.result = margin_error2(probability, data)
        return self.result

    def testSize(self, proportion, probability, precision):
        self.result = testSize(proportion, probability, precision)
        return self.result

    def TestWithoutStandDevi(self, proportion, probability, precision):
        self.result = TestWithoutStandDevi(proportion, probability, precision)
        return self.result

    def sample_random_sampling(self, data, sample_size):
        self.result = population(data, sample_size)
        return self.result

    def c_interval_bottom(self, probability, data):
        self.result = confidence_interval_bottom(probability, data)
        return self.result

    def me(self, probability, data):
        self.result = margin_error2(probability, data)
        return self.result

    def testSize(self, proportion, probability, precision):
        self.result = testSize(proportion, probability, precision)
        return self.result

    def TestWithoutStandDevi(self, proportion, probability, precision):
        self.result = TestWithoutStandDevi(proportion, probability, precision)
        return self.result
