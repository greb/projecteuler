def problem6(count):
    gen = xrange(1, count+1)
    sum1 = sum(x**2 for x in gen)
    sum2 = sum(x for x in gen)**2
    return sum2 - sum1

print problem6(100)
    
