import math
from operator import mul

def d(n):
    string = ""
    i = 0
    while i<n:
        i = i + 1
        string = string + str(i)
    return int(string[n-1])

def problem40():
    return reduce(mul, [d(10**x) for x in xrange(7)])

print problem40() 

