def problem1(max):
    return sum([x for x in xrange(max) if not x%3 or not x%5])

upper_bound = 1000
print "The Summ of all numbers under", upper_bound, \
        "which are mulitples of 3 or 5 is", problem1(upper_bound)


