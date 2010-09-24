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


def problem3(number):
    prime_gen = prime()
    p = 0
    while number > 1:
        p = prime_gen.next()
        while number%p == 0:
            number = number / p
    return p

print problem3(600851475143)
