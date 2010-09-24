def score(pair):
    print pair
    rank, name = pair
    rank = rank + 1
    sum = 0
    for c in name:
        c = ord(c)
        if c >= ord("A") and c <= ord("Z"):
            sum = sum + c - 64
    return sum*rank

file = open("names.txt", "r")
data = file.readlines()[0]
file.close()
names = sorted(data.split(","))
assert score((937,"\"COLIN\"")) == 49714
print sum(map(score, enumerate(names)))
