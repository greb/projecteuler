def problem48():
    n = str(sum([ (x+1)**(x+1) for x in range(1000)]))
    return n[len(n)-10:]

print problem48()

