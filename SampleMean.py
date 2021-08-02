from Addition import addition
from Division import division
from Getsample import getSample


def sample_mean(data, sample_size):
    total = 0
    sample = getSample(data, sample_size)
    num_values = len(sample)
    for num in sample:
        total = addition(total, num)
    return division(total, num_values)
