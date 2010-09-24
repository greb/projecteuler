from eulerhelper import permutation, factorial

def is_pandigital(string):
    string = "".join(sorted([c for c in string]))
    if string == "123456789":
        return True
    return False

def problem38():
    result = []
    for x in xrange(10000):
        for y in xrange(7):
            n = ""
            for i in xrange(1,y):
                n = n + str(i*x)
                if len(n) > 9:
                    break
            if is_pandigital(n):
                result.append(n)
    return max(result)

print problem38()
