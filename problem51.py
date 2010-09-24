from math import log10
from eulerhelper import timed, prime_sieve

limit = 10**6
sieve = prime_sieve(limit)

def replace(number, digit):
    repl = str(number)
    repl = repl.replace("1", str(digit))
    return int(repl)

def count_primes(number):
    result = []
    l = lambda n: int(log10(n))
    ln = l(number)
    for x in xrange(10):
        repl = replace(number, x)
        if sieve[repl] and l(repl) == ln:
            result.append(repl)
    return result

@timed
def problem51():
    for n in xrange(10001, limit, 2):
        if sieve[n]:
            count = count_primes(n)
            if len(count) == 8:
                return count[0] 

print problem51()
