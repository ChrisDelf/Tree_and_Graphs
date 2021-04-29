def visitedCheck(matrix, visited , i, j):
    ## this will establish our start point
    result = False;
    
    if matrix[i][j] != 0:
        
        room_string = ""
        room_string += str(i)
        room_string += str(j)
        
       
        ## going to added to visited
        
        if room_string not in visited:
            visited[room_string] = matrix[i][j]
            result = visited
            return visited
        ## if it is already in visted we should break
        else:
           
            return False;
    else:
        return result
        
    

def matrixElementsSum(matrix):
    ## the rooms must be connect to each other
    ## we want the max amout for rooms that the bots can buy
    
    ## going the need pointer that keeps track of the start point
    ## also we have to keep track of visited rooms
    
    visited = {}
    result = 0
    number_of_rooms = 0
    value_of_rooms = 0
    for i in range(len(matrix)):
        
        for j in range(len(matrix[i])):
            
            result = visitedCheck(matrix, visited , i, j)
            if result != False:
                visited = result
                ## now we should check the y axis
                if i+1 < len(matrix) - 1: 
                    for y in range(i+1, len(matrix)):
                        result = visitedCheck(matrix, visited , y, j)
                        if result != False:
                            visited = result 
                ## now for the x axis
                if j+1 < len(matrix[0]) - 1:
                    for x in range(j+1, len(matrix[0])):
                        result = visitedCheck(matrix, visited , i, x)
                        if result != False:
                            visited = result
               
        ## now we shall tally up all of the rooms and values we have gotten
        temp_sum = 0
        for key in visited:
            temp_sum += visited.get(key)
        if len(visited) > number_of_rooms:
            number_of_rooms = len(visited)
            value_of_rooms = temp_sum
            
        ## now we need to clear the dictionary
        visited = {}
        
        return value_of_rooms
        
