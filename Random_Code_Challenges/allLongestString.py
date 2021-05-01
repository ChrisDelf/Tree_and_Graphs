def allLongestStrings(inputArray):
    ## we are going to need to iterate through the input twice
    
    
    
    returnArray = []
    max_length = 0
    
    ## once to find the maximum length
    for i in range(len(inputArray)):
        if len(inputArray[i]) > max_length:
            max_length = len(inputArray[i])
    
    ## another create a return array
    for j in range(len(inputArray)):
        if len(inputArray[j]) == max_length:
            returnArray.append(inputArray[j])
    
    return returnArray
    
