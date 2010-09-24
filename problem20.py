def fak(n):
    fak = 1
    while n > 1:
        fak = fak * n
        n = n - 1
    return fak

print sum( int(x) for x in str(fak(100)))
