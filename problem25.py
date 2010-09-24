from eulerhelper import fibonacci_generator

def problem25():
    fibonacci = fibonacci_generator()
    fib = 0
    result = 0
    while len(str(fib)) < 1000:
        result = result + 1
        fib = fibonacci.next()
    return (result, fib, len(str(fib)))

print problem25()

