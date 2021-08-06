def differentSymbolsNaive(s):
    ## going to use a dictionary for this one
    differentL = {}
    for letter in s:
        if letter not in differentL:
            differentL[letter] = 0
    if len(differentL) > 0:
        return len(differentL)
    else:
        return 0
