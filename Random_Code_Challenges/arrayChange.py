def arrayChange(inputArray):
    ## previous element
    prevE = 0
    temp_counter = 0
    moves = 0
    checkingC = 0
    
    for i in range(len(inputArray)):
        
        ## if we its equal to the previous value we increment by 1
        if prevE == inputArray[i] and i != 0:
            temp_counter += 1
            prevE = prevE + temp_counter
            moves = moves + temp_counter
        ## if not we have to find the difference
        elif prevE > inputArray[i] and i != 0:
            temp_counter = prevE - inputArray[i] + 1
            ## if the element is a negative value we have to use absloute value
            if inputArray[i] < 0:
                prevE = temp_counter - abs(inputArray[i])
            ## this is for elements that are not negative
            else:
                prevE = temp_counter + inputArray[i]
                
            moves = moves + temp_counter
        ## if the value is already greater than the previous value we don't need to make any moves
        else:
            prevE = inputArray[i]
        
        temp_counter = 0
        
    return moves
            
