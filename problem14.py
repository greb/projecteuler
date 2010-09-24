def collatz(number):
    count = 1
    while number > 1:
        if number%2 == 0:
            number = number / 2
        else:
            number = 3*number + 1
        count = count + 1
    return count

def problem14():
    m = 0
    max = 0
    for x in xrange(1,10**6):
        c = collatz(x)
        print "%6d %4d %6d %4d" % (x, c, max, m)
        if c > m:
            m = c
            max = x
    return max

print problem14()

