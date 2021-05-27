def avoidObstacles(inputArray):

    i=0
    increment=1
    while(i<max(inputArray)):
        i+=increment
        if i in inputArray:
            i=0
            increment+=1
    return increment
