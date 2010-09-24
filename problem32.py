def is_pandigital_9(m1,m2,prod):
    number = str(m1) + str(m2) + str(prod)
    if len(number) != 9:
        return False

    number = "".join(sorted([c for c in number]))
    if number == "123456789":
        return True
    else:
        return False

def problem32():
    result = []
    for i in xrange(10000):
        for j in xrange(1000):
            if is_pandigital_9(i,j,i*j):
                result.append(i*j)
    return sum(set(result))


print problem32()
