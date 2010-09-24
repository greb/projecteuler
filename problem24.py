from eulerhelper import factorial

def permutator(digits, permutation):
    result = ""
    digits = [c for c in digits]
    while len(digits) > 0:
        selection = factorial(len(digits)-1)
        index = permutation / selection
        permutation = permutation % selection
        result = result + digits[index]
        del digits[index]
    return result

def problem24():
    return permutator("0123456789", 10**6-1)

print problem24()
