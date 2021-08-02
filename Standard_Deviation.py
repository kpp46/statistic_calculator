from Variance import variance
from Square_root import sqr
from check_emptylist import check


def stddev(data):
    data = check(data)
    var = variance(data)
    squareroot = sqr(var)
    return squareroot
