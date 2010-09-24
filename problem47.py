from eulerhelper import prime_factors, prime_sieve
from operator import mul

sieve_max = 10**6
sieve = prime_sieve(sieve_max)
primes = [] 
for x in xrange(sieve_max):
    if sieve[x]:
        primes.append(x)

def factors(n):
    facs = []
    for p in primes:
        if n == 1:
            break
        if n%p == 0:
            facs.append(p)
            while n%p == 0:
                n = n / p
    return facs

def problem47():
    i = 0
    size = 4 
    numbers = []
    while True:
        i = i + 1
        print i
        numbers.append(len(factors(i)))
        if len(numbers) > size:
            del numbers[0]
            if sum(numbers) == size*size:
                return i-size+1

print problem47()

