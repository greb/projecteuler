import math
import time

# special numbers

def fibonacci_generator():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

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

def prime_sieve(max=1000):
    sieve = [1]*max
    pos = 2
    sieve[0] = 0
    sieve[1] = 0
    while pos < max:
        while sieve[pos] == 0 and pos < max -1:
            pos = pos + 1
        for x in range(pos*2, max, pos):
            sieve[x] = 0
        pos = pos + 1
    return sieve

def prime_generator(max=0):
    stored_primes = [] 
    prime = 2

    def is_prime(number):
        for prime in stored_primes:
            if prime > math.sqrt(number):
                return True
            if number%prime == 0:
                return False
        return True

    while max == 0 or max >= prime:
        stored_primes.append(prime)
        yield prime
        if prime < 3:
            prime = prime + 1
        else:
            prime = prime + 2
            while not is_prime(prime):
                prime = prime + 2

def trigonal(n):
    return n*(n+1)/2

def pentagonal(n):
    return n*(3*n-1)/2

def hexagonal(n):
    return n*(2*n-1)

def inv_trigonal(n):
    return int((math.sqrt(8*n + 1) - 1.0) / 2.0)

def inv_pentagonal(n):
    return int((math.sqrt(24*n + 1) + 1.0) / 6.0)

def inv_hexagonal(n):
    return int((math.sqrt(8*n + 1) + 1.0) / 4.0)

def is_trigonal(n):
    n = (math.sqrt(8*n + 1) - 1.0) / 2.0
    return int(n) == n 

def is_pentagonal(n):
    n = (math.sqrt(24*n + 1) + 1.0) / 6.0
    return int(n) == n

def is_hexagonal(n):
    n = (math.sqrt(8*n + 1) + 1.0) / 4.0
    return int(n) == n



# combinatorics

def factorial(n):
    if n <= 1:
        return 1
    fac = 1
    while n > 1:
        fac = fac * n
        n = n - 1
    return fac

def combination(n,k):
    return factorial(n) / factorial(k) / factorial(n-k)

def permutation(string, index):
    result = ""
    string = [c for c in string]
    while len(string) > 0:
        fac = factorial(len(string)-1)
        next = index / fac
        index = index % fac
        result = result + string[next]
        del string[next]
    return result
     

# factorize

def proper_factors_sum(n):
    if n == 1:
        return 0
    root = int(math.sqrt(n))
    sum = 1 
    if root**2 == n:
        sum = sum + root
        root = root - 1 
    start = 2 
    step  = 1 
    if n%2 == 1:
        start = 3 
        step = 2 
    for x in xrange(start, root+1, step):
        if n%x == 0:
            sum = sum + x + n/x 
    return sum 

def proper_factors(n):
    if n == 1:
        return []
    factors = [1]
    root = int(math.sqrt(n))
    if root**2 == n:
        factors.append(root)
        root = root - 1 
    start = 2 
    step  = 1 
    if n%2 == 1:
        start = 3 
        step = 2 
    for x in xrange(start, root+1, step):
        if n%x == 0:
            factors.append(x)
            factors.append(n/x)
    return list(sorted(factors))

def prime_factors(n):
    factors = []
    if n < 2:
        return factors
    primes = prime_generator()
    while True:
        p = primes.next()
        while n%p == 0:
            factors.append(p)
            n = n / p
        if n == 1:
            break
    return factors

def prime_factors_list(n, primelist):
    factors = []
    p = 0
    if n < 2:
        return factors
    while n > 1:
        prime = primelist[p]
        while n%prime == 0:
            factors.append(prime)
            n = n / prime
        p = p + 1
    return factors


# misc

def timed(fn):
    def timed_function(*args, **kwds):
        _time_start = time.time()
        _return = fn(*args, **kwds)
        print int(1000*(time.time()-_time_start)), "ms"
        return _return
    return timed_function
