import math
max = 10000

propfactor = lambda n: [x for x in xrange(1,n/2+1) if n%x==0]
pairs = map(lambda x: (x,sum(propfactor(x))), xrange(1, max+1)) 
amicible = filter(lambda x: sum(propfactor(x[1])) == x[0] and x[0] != x[1],pairs)
result = sum(map(lambda x: x[0], amicible))

print result 

