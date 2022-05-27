def solution(matrix):
    #lets check the length of the matrix
    matrixL= 0
    #going to need a set to store our results
    resultSet= set()
    
    if len(matrix) < 2:
        return 0;
    else:
        matrixL = len(matrix)
    
    if len(matrix[0]) < 2:
        return 0
    
    for x in range(0, matrixL - 1):
        current_array = matrix[x]
        current_length = len(current_array)
        for i in range(0, current_length - 1):
            boxString = str(current_array[i])
            
            #now we need checks for right, bottom, bottom right
            
            #right
            if matrix[x][i+1] != None:
                boxString = boxString + str(matrix[x][i+1])
                #bottom
                if matrix[x-1][i] != None:
                    boxString = boxString + str(matrix[x-1][i])
                    #bottom right
                    if matrix[x+1][i+1] != None:
                        boxString = boxString + str(matrix[x+1][i+1])
                        # now we add it to our set
                        if boxString not in resultSet:
                            resultSet.add(boxString)
                              
    return len(resultSet)
