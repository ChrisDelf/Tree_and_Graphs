def commonCharacterCount(s1, s2):
    
    ## first iteration we will create a dictionary
    comparsionDict = {}
    counter = 0
    for i in range(len(s1)):
        if s1[i] not in comparsionDict:
            comparsionDict[s1[i]] = 0
            comparsionDict[s1[i]] = 1
        else:
            comparsionDict[s1[i]] += 1
            
    ## now to iterate through the second dictionary
    for j in range(len(s2)):
        if s2[j] in comparsionDict:
           if comparsionDict[s2[j]] > 0:
                counter += 1
                comparsionDict[s2[j]] -= 1
            
            
    return counter
