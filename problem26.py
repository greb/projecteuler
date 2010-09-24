count = 1000

def cycle(n):
    q = [0]
    r = [1]
    for i in xrange(1, count):
        q.append(r[i-1]*10 / n)
        r.append(r[i-1]*10 % n)
        for j in xrange(1,i):
            if q[i] == q[j] and r[i] == r[j]:
                return i-j

def problem26():
    max = 0
    result = 0
    for x in xrange(1, count):
        if cycle(x) > max:
            max = cycle(x)
            result= x
    return result

print problem26()

    
