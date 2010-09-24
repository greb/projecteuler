def divisors(n):
    i = 0
    for x in xrange(1,n+1):
        if n%x == 0:
            i = i+1
    return i

def square_triangle(n):
    s = 1
    for x in xrange(1,n):
        s = 4*s*(8 * s + 1)
    return s

def problem12():
    return divisors(square_triangle(4))

print problem12() 
