def problem29():
    return len(set([a**b for a in xrange(2,101) for b in xrange(2,101)]))

print problem29()
