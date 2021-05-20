def arrayMaximalAdjacentDifference(inputArray):
    maxDif = 0
    
    ## so we are going to have a lagging pointer and next pointer
    lagP = 0
    nextP = 0
    
    for i in range(0, len(inputArray)):
        nextP = i + 1
        
        if nextP >= len(inputArray):
            break
        
        lagE = inputArray[lagP]
        nextE = inputArray[nextP]
        currentE = inputArray[i]
        ## comparing the laggingP to current
        if abs(lagE - currentE) > maxDif:
            print("lag",lagE - currentE)
            maxDif = abs(lagE - currentE)
        
        ## comparing the nextP to current
        if abs(nextE - currentE) > maxDif:
            print("next", nextE - currentE)
            maxDif = abs(nextE - currentE)
            
        lagP += 1
    
    return maxDif
