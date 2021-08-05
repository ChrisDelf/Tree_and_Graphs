def extractEachKth(inputArray, k):
    ##going to interate through the array and create a new array that does not include anything divisble by k
    resultA = []
    for i in range(len(inputArray)):
       
        if (i+1) % k != 0:
            
            resultA.append(inputArray[i])
        
    return resultA

