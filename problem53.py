from eulerhelper import combination, timed

@timed
def problem53():
    count = 0
    for n in xrange(1, 101):
        for r in xrange(n+1):
            if combination(n,r) > 10**6:
                count = count + 1
    return count

print problem53()
