def wordvalue(word):
    value = 0
    for c in word:
        value = value + ord(c)-ord("A") + 1
    return value

def problem42():
    triangles = [ n*(n+1)/2 for n in xrange(1,1000)]
    file = open("words.txt")
    words = [w.strip("\"\n") for w in file.read().split(",")] 
    triwords = [w for w in words if wordvalue(w) in triangles]
    return len(triwords)

print problem42()
