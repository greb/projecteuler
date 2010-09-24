from eulerhelper import *

def solve(money):
    coins = [1,2,5,10,20,50,100,200]
    def find(money, maxcoin):
        sum = 0
        if maxcoin == 7: return 1
        for i in xrange(maxcoin, 8):
            diff = money - coins[i]
            if diff == 0:
                sum = sum + 1
            if diff > 0:
                sum = sum + find(diff, i)
        return sum
    return find(money, 0)

def problem31():
    return solve(200)
    
    
print problem31()
