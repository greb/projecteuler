digits = ["one", "two", "three", 
       "four", "five", "six",
       "seven", "eight", "nine"]

decades = ["ten", "twenty", "thirty",
        "forty", "fifty", "sixty",
        "seventy", "eighty", "ninety"]

teeners = ["eleven", "tvelve", "thirteen",
          "fourteen", "fifteen", "sixteen",
          "seventeen", "eighteen", "nineteen"]

def say_in_words(n):
    if n <= 0:
        return ""
    elif n < 10:
        return digits[n-1]
    elif n < 20 and n != 10:
        return teeners[n-11]
    elif n < 100:
        return decades[(n/10)-1] + say_in_words(n%10)
    elif n < 1000:
        r = digits[(n/100)-1] + "hundred"
        if n%100 > 0:
            return r + "and" + say_in_words(n%100)
        return r
    elif n < 10000:
        return digits[(n/1000)-1] + "thousand" + say_in_words(n%1000)

def problem17(n):
    return sum( ( len(say_in_words(x)) for x in xrange(1, n+1) ) )

print problem17(1000)
