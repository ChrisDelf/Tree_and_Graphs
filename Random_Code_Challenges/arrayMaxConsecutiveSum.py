
def arrayMaxConsecutiveSum(inputArray, k):
    ## going to have a ahead pointer
    currentI = 0
    nextI = k
    consSum = None
    if len(inputArray) < 1:
        return None
    
    while nextI <= len(inputArray) -1:
        
        tempArray = inputArray[currentI:nextI]
        tempSum = 0
        
        
        for i in range(len(tempArray)):
            tempSum += tempArray[i]
 
        
        if consSum == None or tempSum > consSum:
            consSum = tempSum
        
        currentI += 1
        nextI += 1
        if nextI > len(inputArray) - 1:
            tempArray = inputArray[currentI:len(inputArray)]
            tempSum = 0
           
        
            for j in range(len(tempArray)):
                tempSum += tempArray[j]
 
            
            if consSum == None or tempSum > consSum:
                consSum = tempSum
        
        
                
    return consSum
