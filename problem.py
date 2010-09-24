from eulerhelper import prime_sieve

limit = 10**6
sieve = prime_sieve(limit)
primes = [x for x in xrange(limit) if sieve[x]]

def count_additions(n, p):
    count = 0
    while n > 0:
        count = count + 1
        n = n - primes[p] 
        p = p + 1
    return count, n

def problem50():
    result = 0
    max = 0
    for n in xrange(limit):
        print n
        if sieve[n] == 1:
            stop = 10 
            for p in xrange(0, stop):
                additions, diff = count_additions(n, p)
                if diff == 0 and additions > max:
                    max = additions
                    result = n
    return result
        
print problem50()
