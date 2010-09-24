from math import sqrt
from eulerhelper import hexagonal, inv_hexagonal
from eulerhelper import is_trigonal, is_pentagonal

assert 40755 == hexagonal(inv_hexagonal(40755))
assert is_trigonal(40755) and is_pentagonal(40755)

def problem45():
    n = 40755
    while True:
        n = hexagonal(inv_hexagonal(n)+1)
        if is_pentagonal(n) and is_trigonal(n):
            return n

print problem45()
