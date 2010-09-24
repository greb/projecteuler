from eulerhelper import timed

limit = 10**6

def compare_numbers(n1, n2):
    n1, n2 = str(n1), str(n2)
    order = lambda n: "".join(sorted([c for c in n]))
    return order(n1)==order(n2)

def check_number(number):
    for x in xrange(2,7):
        if not compare_numbers(number, x*number):
            return False
    return True

@timed
def problem52():
    for x in xrange(1, limit):
        if check_number(x):
            return x

print problem52()
