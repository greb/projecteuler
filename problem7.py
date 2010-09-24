def isPrime(number, primes):
    for x in [p for p in primes if p <= number/2]:
        if number%x == 0:
            return False
    return True

def prime():
    primes = []
    p = 2
    while(True):
        if len(primes) > 0:
            p = p + 1
            while not isPrime(p, primes):
                p = p + 1
        primes.append(p)
        yield p


def problem7(number):
    prime_gen = prime()
    for x in xrange(number-1):
        prime_gen.next()
    return prime_gen.next()

print problem7(10001)
