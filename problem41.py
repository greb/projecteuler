import math
from eulerhelper import permutation, factorial

def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True
    
    if n%2 == 0:
        return False

    p = 3 
    while p <= math.sqrt(n):
        if n%p == 0:
            return False
        p = p + 2
    return True

def problem41():
    pandigit = "987654321"
    for i in xrange(9):
        for x in xrange(factorial(9-i)-1):
            if is_prime(int(permutation(pandigit[i:], x))):
                return permutation(pandigit[i:], x)

print problem41()
