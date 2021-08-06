def firstDigit(inputString):
    tempA = list(inputString)
    
    for i in range(len(tempA)):
        if tempA[i].isnumeric() == True:
            return tempA[i]
