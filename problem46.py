from eulerhelper import prime_generator
from math import sqrt, floor

def problem46():
    max = 10**4
    primes = [x for x in prime_generator(max)]
    number = 3

    while number < max:
        number = number + 2 
        if number in primes:
            continue
        valid = 0
        for x in primes:
            if x >= number:
                break
            test = number - x
            square = sqrt(test/2)
            if test%2 == 0 and floor(square) == square:
                valid = 1
                break

        if valid == 0:
            return number

    return 0
print problem46()
                
