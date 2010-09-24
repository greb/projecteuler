import math

def prime(max):
    primes = []
    p = 2 
    
    def is_prime(number):
        for p in primes:
            if p > math.sqrt(number):
                return True
            if number%p == 0:
                return False
        return True

    while(p < max):
        primes.append(p)
        yield p
        if p < 3:
            p = p + 1
        else:
            p = p + 2
            while not is_prime(p):
                p = p + 2

def problem10():
    prime_gen = prime(2*10**6)
    return sum(prime_gen)

print problem10()
