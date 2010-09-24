def bin(n, min_length=0):
    bin = ""
    digits = 0
    while n > 0:
        bin = str(n%2) + bin
        n = n/2
        digits = digits + 1
    if min_length > digits:
        bin = (min_length-digits)*"0" + bin
    return bin 

def solve_slow(n):
    solutions = 0
    n = n * 2
    for x in xrange(2**n):
        path = bin(x,n)
        if path.count("0") == path.count("1"):
            solutions = solutions + 1
    return solutions
    
def fac(n):
    r = 1
    while n>0:
        r = r * n
        n = n -1
    return r

def binom(n, k):
    return fac(n) / fac(k) / fac(n-k)

def problem15(n):
    for x in xrange(1,n+1):
        print x, binom(x*2,x)

problem15(20)
