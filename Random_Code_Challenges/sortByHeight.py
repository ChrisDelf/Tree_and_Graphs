def sortByHeight(a):
    ## we are going to create a new array 
    ## going to ignore the -1 since there are trees
    
    returnArray = []
    highestValue = None
    lowerValue = None
    isLowest = False
    alreadyPlaced = {}
    for i in range(len(a)):
        if a[i] != -1:
            for x in range(i, len(a)):
                ## we need to do a comparison
                if a[i] > a[x] and a[x] != -1:
                    isLowest = False
                    if lowerValue == None or lowerValue > a[x]:
                        print(a[i],a[x])
                        lowerValue = a[x]
                    if highestValue == None or highestValue < a[i]:
                        highestValue = a[i]
                else:
                    isLowest = True
                    lowerValue = a[i]
            
            
            if isLowest == True:
                if a[i] not in alreadyPlaced:
                    alreadyPlaced[a[i]] = 0
                    returnArray.append(a[i])
                    isLowest = False
            else:
                if a[i] not in alreadyPlaced:
                    alreadyPlaced[lowerValue]= 0
                    returnArray.append(lowerValue)
            
