from Mean import mean
from Square import sq
# from Division import division
# from Addition import addition
from Subtraction import subtraction
from check_emptylist import check


def variance(data):
    data = check(data)
    average = mean(data)
    a = []
    for i in data:
        a.append(sq(subtraction(average, i)))
    return mean(a)
