def is_palindrome(string):
    return string == string[::-1]

def bin(number):
    b = ""
    while number > 0:
        b = str(number%2) + b
        number = number / 2
    return b

assert is_palindrome("reliefpfeiler")
assert bin(23) == "10111"

def problem36():
    result = []
    for x in xrange(10**6):
        if is_palindrome(str(x)) and is_palindrome(bin(x)):
            result.append(x)
    return sum(result)

print problem36()
