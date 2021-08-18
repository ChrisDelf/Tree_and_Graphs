def knapsackLight(value1, weight1, value2, weight2, maxW):
    ## fist check we can do is to see if the maxW is greater than combine weight
    
    if maxW >= (weight1+weight2):
        return value1 + value2
    ## need see if we can take any of the treasure
    tempA = [weight1,weight2]
    for x in range(0,2):
        
        if tempA[x] > maxW:
            tempA.append(x)
            
    ## if the length is four then we know that all the ojbects are too heavy
    if len(tempA) == 4:
        print(tempA)
        return 0
        
        
    ## crate ratio to tell us which treasure to check
    valueR1 = value1/weight1
    valueR2 = value2/weight2
    
    
      
    if valueR1 >= valueR2:
        return value1
    else:
        return value2

