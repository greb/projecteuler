from eulerhelper import factorial

def is_curious(n):
    sum = 0
    for c in str(n):
        sum = sum + factorial(int(c))
    if sum == n:
        return True
    else:
        return False

def problem34():
    result = []
    for x in xrange(3, factorial(9)):
        if is_curious(x):
            result.append(x)
    return sum(result)

print problem34()
    
