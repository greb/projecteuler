def is_curious(x,y):
    if x >= y:
        return False
    
    x1, x2 = x/10, x%10
    y1, y2 = y/10, y%10

    if x1 == 0 or x2 == 0 or y2 == 0 or y2 == 0:
        return False

    if x1 == y1:
        x_, y_ = x2, y2
    elif x2 == y2:
        x_, y_ = x1, x1
    elif x1 == y2:
        x_, y_ = x2, y1
    elif x2 == y1:
        x_, y_ = x1, y2
    else:
        return False
    
    if (x*y_)/x_ == y:
        return True
    else:
        return False

def problem33():
    result = []
    for x in range(10,100):
        for y in range(10, 100):
            if is_curious(x, y):
                result.append((x,y))
    product = reduce(lambda a, b: (a[0]*b[0], a[1]*b[1]), result)
    return product[1] / product[0]

print problem33()
