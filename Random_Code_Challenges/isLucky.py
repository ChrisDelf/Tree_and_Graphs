def isLucky(n):
    ## we need to convert n into an array:
    nArray = []
    for i in str(n):
        nArray.append(int(i))
    
    ## now we can find the midpoint
    midpoint = int(len(nArray) / 2)
    
    ## with the midpoint we can seperate the array
    left_array = nArray[:midpoint]
    right_array = nArray[midpoint:]
    
    leftSum = 0
    rightSum = 0
    x = 0
    ## now for the iteration:
    for j in range(len(nArray)):
        if j < midpoint:
            leftSum = leftSum + left_array[j]
        if j >= midpoint:
            rightSum = rightSum + right_array[x]
            x += 1
        if rightSum > leftSum:
            return False;
    
    if leftSum == rightSum:
        return True;
    else:
        return False;
    
