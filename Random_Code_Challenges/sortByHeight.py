def sortByHeight(a):
    minus_one_position = []
    for i in range(len(a)):
        if a[i]== -1:
            minus_one_position.append(i)
    for i in range(len(minus_one_position)):
        a.remove(-1)
    b = sorted(a)
    for i in range(len(minus_one_position)):
        b.insert(minus_one_position[i], -1)
    return b
