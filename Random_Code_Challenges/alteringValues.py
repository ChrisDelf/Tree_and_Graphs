def alternatingSums(a):
    ## going to use a pointer for every other index
    first_p = 0
    second_p = 1
    
    ## we are going to have two variables for the separated sums
    firstSum = 0
    secondSum = 0
    
    fAtEnd = False
    sAtEnd = False
    ## now we are going to iterrate through the array
    
    for i in range(0, len(a)):
        
        
        if first_p <= len(a)-1 and fAtEnd == False:
            firstSum = firstSum + a[first_p]
        else:
            fAtEnd = True
            
        
        if second_p > len(a)-1:
            sAtEnd = True
            
        elif second_p == len(a)-1:
            secondSum = secondSum + a[second_p]
            
        elif second_p <= len(a)-1 and sAtEnd == False:
            
            secondSum = secondSum + a[second_p]
        
        first_p = first_p + 2
        second_p = second_p + 2
        
        
    
    resultArray = []
    
    resultArray.append(firstSum)
    resultArray.append(secondSum)
    
    return resultArray
            
        
            
