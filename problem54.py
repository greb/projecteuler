
def max_value(cards):
    return cards[-1][0]

def consective(cards):
    card0 = cards[0][0]
    for x in xrange(1,len(cards)):
        card0 = card0 + 1
        if card0 != cards[x][0]:
            return None
    return card0

def same_suit(cards):
    card0 = cards[0][1]
    for x in xrange(1,len(cards)):
        if card0 != cards[x][1]:
            return False
    return True

def same_value(cards):
    card0 = cards[0][0]
    for x in xrange(1, len(cards)):
        if card0 != cards[x][0]:
            return False
    return True

def repetitive(cards):
    result = []
    found = []
    for n in xrange(4, 1, -1):
        for o in xrange(len(cards)-n+1):
            if same_value(cards[o:o+n]) and cards[o][0] not in found:
                found.append(cards[o][0])
                result.append((n, cards[o][0]))
    
    return result

def hand_value(hand):
    v = "x23456789TJQKA"
    s = "CDHS"
    l = len(v)
    cards = map(lambda x: (v.index(x[0]), s.index(x[1])), hand)
    cards = sorted(cards, lambda a, b: cmp(a[0],b[0]))

    con = consective(cards)
    same = same_suit(cards)
    rep = repetitive(cards)
    
    if con == v.index("A") and same:
        print "Royal Flush"
        return l**9
    elif con != None and same:
        print "Straigth Flush"
        return l**8 * con
    elif len(rep) == 1  and rep[0][0] == 4:
        print "Four of a Kind"
        return l**7 * rep[0][1]
    elif len(rep) == 2 and rep[0][0] == 3 and rep[1][0] == 2:
        print "Full House"
        return l**6 * max(rep[0][1], rep[1][1])
    elif same:
        print "Flush"
        return l**5 * max_value(cards)
    elif con != None:
        print "Straigth"
        return l**4 * con
    elif len(rep) == 1 and rep[0][0] == 3:
        print "Three of a Kind"
        return l**3 * rep[0][1]
    elif len(rep) == 2 and rep[0][0] == 2 and rep[1][0] == 2:
        print "Two Pairs"
        return l**2 * max(rep[0][1], rep[1][1])
    elif len(rep) == 1 and rep[0][0] == 2:
        print "One Pair"
        return l**1 * rep[0][1]
    else:
        print "High Card"
        return max_value(cards)


def parse_file(filepath):
    file = open(filepath, "r")
    lines = map(lambda x: x.strip("\n\r").split(" "), file.readlines())
    file.close()
    hands = map(lambda x: (x[:5],x[5:]), lines)
    return hands

def problem54():
    data = parse_file("poker.txt")
    player1_wins = 0
    for hand in data:
        if hand_value(hand[0]) > hand_value(hand[1]):
            player1_wins = player1_wins + 1
    return player1_wins
    
print problem54()
