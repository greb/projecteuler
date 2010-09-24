from eulerhelper import *

def problem23(limit):

    numbers = list(xrange(1, limit+1))
    abundant_numbers = filter(lambda x: proper_factors_sum(x) > x, numbers)

    length = len(abundant_numbers)
    for i in xrange(length):
        for j in xrange(i, length):
            index = abundant_numbers[i] + abundant_numbers[j] - 1
            if index < limit and numbers[index]:
                numbers[index] = 0

    return sum(numbers)

print problem23(28123)
