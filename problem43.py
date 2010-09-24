from eulerhelper import factorial, permutation, prime_generator

primes = [x for x in prime_generator(17)]

def divisiontest(number):
    for x in xrange(7):
        if int(number[x+1:x+4]) % primes[x] != 0:
            return False
    return True

assert divisiontest("1406357289")

def problem42():
    result = []
    pandigit = "0123456789"
    for x in xrange(factorial(10)-1):
        number = permutation(pandigit,x)
        if divisiontest(number):
            result.append(int(number))
    return sum(result)

print problem42()
