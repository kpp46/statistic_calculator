from Addition import addition
from Division import division
from Multipule import mul
from Square import sq
from Square_root import sqr
from Subtraction import subtraction


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def division(self, a, b):
        self.result = division(a, b)
        return self.result

    def mul(self, a, b):
        self.result = mul(a, b)
        return self.result

    def sq(self, a):
        self.result = sq(a)
        return self.result

    def sqr(self, a):
        self.result = sqr(a)
        return self.result
