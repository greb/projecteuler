def problem44():
    pairs = [] 
    pentagonal = set([n*(3*n-1)/2 for n in xrange(1,10000)])
    for k in pentagonal:
        for j in pentagonal:
            if j>= k:
                continue  
            if j+k in pentagonal and abs(j-k) in pentagonal:
                pairs.append((j,k))              
    
    result = sorted(map(lambda a: abs(a[0]-a[1]), pairs))
    return result[0]

print problem44()
