def problem9():
    gen = xrange(1,1000)
    catheti_gen = ( (a,b) for a in gen for b in gen)
    for a,b in catheti_gen:
        h = 1000 - a - b
        if h**2 == a**2 + b**2:
            return a*b*h 
    return 0

print problem9()
