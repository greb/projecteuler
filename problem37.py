from eulerhelper import prime_generator

def problem37():

    max = 1000000
    primes = set([x for x in prime_generator(max)])
    result = []
    
    def is_truncable_prime(n):
        n = str(n)
        l = len(n)
        for i in xrange(l):
            if int(n[l-i-1:]) not in primes or int(n[:i+1]) not in primes:
                return False
        return True

    for x in xrange(10, max):
        print x
        if is_truncable_prime(x):
            result.append(x)
    print result, len(result)
    return sum(result)
        

print problem37()
