import math

def triangle(p):
    tri = []
    min_c = float(p) / (2.0 + math.sqrt(2)) * math.sqrt(2)
    min_b = float(p) / (2.0 + math.sqrt(2))
    for c in xrange(int(min_c), p):
        for b in xrange(int(min_b), p-c):
            for a in xrange(1, b):
                if a+b+c > p:
                    break
                if a+b+c == p and a*a + b*b == c*c:
                    tri.append((a,b,c))
    return tri

def problem39():
    result = 0
    max = 0
    for p in xrange(12, 1000):
        tri = len(triangle(p))
        print p, tri
        if tri > max:
            max = tri
            result = p
    return result

print problem39()
