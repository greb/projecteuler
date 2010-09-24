def problem28():
    n = 1
    numbers = [n]
    for i in xrange(2,1001, 2):
        for j in range(4):
            n = n + i
            numbers.append(n)
    return numbers

print sum(problem28())
