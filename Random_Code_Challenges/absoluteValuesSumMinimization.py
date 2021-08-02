def absoluteValuesSumMinimization(a):
    
    i = 0

    lowestDiff = None
    lowestIndex = 0
    while i <= len(a)-1:
        x = a[i]
        diff = 0
        for j in range(0, len(a)):
            diff += abs(a[j] - x)
        
        if lowestDiff == None:
            lowestDiff = diff

        elif diff < lowestDiff:
            lowestDiff = diff
            lowestIndex = i

            
        
            
            
        
        i+=1       

    return a[lowestIndex]
