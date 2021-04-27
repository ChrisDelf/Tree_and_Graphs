##Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
inputArray_2 = [-1, -2]
inputArray = [3, 6, -2, -5, 7, 3]
##adjacentElementsProduct(inputArray) = 21.
##7 and 3 produce the largest product.

def adjacentElementsProduct(inputArray):
    ## going to have to make use of three pointers
    prev = 0
    current_i = 0
    next_i = 0
    ## going to need a variable to store largestProduct
    
    largest_P = None
    
    for i in range(0, len(inputArray)):
        prev = i -1
        current_i = i
        next_i = i + 1
        left = 0
        right = 0
        
        ## this break out of loop once we get to the end
        if next_i > len(inputArray) - 1:
            break;
      
        if prev >= 0:
            ## going to calculate the adjacent Elements
            left = inputArray[prev] * inputArray[current_i]
            right = inputArray[current_i] * inputArray[next_i]
            
          
            
            ## store the largest product
            if largest_P == None or left > largest_P:
                largest_P = left
                
            if largest_P == None or right > largest_P:
                largest_P = right
        else:
            ## if we are at the start we can only check values to the right
            right = inputArray[current_i] * inputArray[next_i] 
            if largest_P == None or right > largest_P:
                largest_P = right
    
    return largest_P
