def problem30():
    digit = 5
    found = []
    for x in xrange(2, 10**(digit+1)):
        sum = 0
        for c in str(x):
            sum = sum + int(c)**digit
        if sum == x:
            found.append(x)
    return found

print sum(problem30())
