def arrayReplace(inputArray, elemToReplace, substitutionElem):
    targetE = elemToReplace
    subE = substitutionElem
    
    for i in range(len(inputArray)):
        if inputArray[i] == targetE:
            inputArray[i] = subE
    
    return inputArray
