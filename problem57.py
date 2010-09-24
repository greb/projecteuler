from math import log10

def expansion(fraction):
    n, d = fraction
    return (n+2*d, n+d)

def is_numerator_longer(fraction):
    n, d = fraction
    if int(log10(n)) > int(log10(d)):
        return True
    else:
        return False

def problem57():
    count = 0
    fraction = (1,1)
    for x in xrange(1000):
        fraction = expansion(fraction)
        if is_numerator_longer(fraction):
            count = count + 1
    return count

print problem57()
