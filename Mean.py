from Addition import addition
from Division import division
from check_emptylist import check


def mean(data):
    data = check(data)
    num_values = len(data)
    total = 0
    for num in data:
        total = addition(total, num)
    return division(num_values, total)
