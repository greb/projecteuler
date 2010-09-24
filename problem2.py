def fib(max):
    a, b = 1, 1
    while(b < max):
        yield b
        a, b = b, a+b

def problem2(max):
    return sum(x for x in fib(max) if not x%2)

upper_bound = 4 * 10**6
print problem2(upper_bound)

