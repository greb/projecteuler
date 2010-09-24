from eulerhelper import permutation, factorial, prime_generator, is_prime

def problem49():
    result = []
    primes = [x for x in prime_generator(10000)]
    d = 3330
    for n in xrange(1000, 10000):
        if n not in primes:
            continue
        n_str = str(n)
        per = [int(permutation(n_str, x)) for x in xrange(factorial(4))]
        pri = [x for x in per if x in primes]
        if n+d in pri and n+2*d in pri:
            result.append(str(n) + str(n+d) + str(n+d+d))
    return list(set(result))

print problem49()
