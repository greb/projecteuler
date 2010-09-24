from eulerhelper import prime_generator

def rotate(string, shift):
    return string[shift:] + string[:shift]

def rotations(string):
    return [rotate(string, i) for i in xrange(len(string))]

def problem35(max):
    done = set() 
    sum = 0
    prime_table = [x for x in prime_generator(max)]
    
    for x in prime_table:
        if x in done:
            continue

        print x

        rs = [int(r) for r in rotations(str(x))]
        if not filter(lambda r: r in prime_table, rs) == rs:
            continue

        for r in rs:
            if r not in done:
                sum = sum + 1
                done.add(r)

    return sum

print problem35(10**6)    
