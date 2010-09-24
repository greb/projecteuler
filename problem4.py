def is_palindrome(number):
    return str(number) == str(number)[::-1]

def problem4():
    pair_gen = (x*y
            for x in xrange(999, 100, -1)
            for y in xrange(999, 100, -1)
            if is_palindrome(x*y))
    return sorted(pair_gen, reverse=True)[0]

print problem4()

