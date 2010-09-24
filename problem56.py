def digit_sum(number):
    return sum([int(x) for x in str(number)])

def problem56():
    limit = 100
    max_sum = 0
    for a in xrange(1, limit):
        for b in xrange(1, limit):
            sum_ab = digit_sum(a**b)
            if sum_ab > max_sum:
                max_sum = sum_ab
                print a, b
    return max_sum

print problem56()
