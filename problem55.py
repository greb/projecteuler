def is_palindrome(number):
    number = str(number)
    return number == number[::-1]

def next_lychrel(number):
    rev = int(str(number)[::-1])
    return rev+number

def is_valid_lychrel(number):
    max_iter = 50
    for x in xrange(max_iter):
        number = next_lychrel(number)
        if is_palindrome(number):
            return False 
    return True

def problem55():
    limit = 10**4
    result = 0
    for n in xrange(1, limit):
        if is_valid_lychrel(n):
            result = result + 1
    return result

print problem55()
