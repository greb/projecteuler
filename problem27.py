from eulerhelper import prime_generator

limit = 10000

prime_table = [x for x in prime_generator(limit)]

def countprimes(a, b):
    count = 0
    for n in xrange(limit):
        x = n*n + a*n + b
        if x > limit:
            print "Warning: limit exceeded. a=", a, "b=", b, "n=", n, "x=", x
        if x in prime_table:
            count = count + 1
        else:
            break
    return count

assert countprimes(1,41) == 40
assert countprimes(-79, 1601) == 80

def problem27():
    start = -1000
    end = 1000
    max = 0
    result = (0,0)

    for a in xrange(start, end+1):
        for b in xrange(start, end+1):
            count = countprimes(a, b)
            print a, b, count
            if count > max:
                max = count
                result = (a, b)
    print result, max
    return result[0] * result[1]

print problem27()
