def travsGrid(matrix, y, x, visited, stack, roomsVisited, totalCost):
    visitedCopy = {}
    
    while len(stack) != 0:
        coors = stack.pop()
        coorsString = str(coors)
        #print(coors)
        
        
        if coorsString not in visited:
            #print("room found", coorsString, "room value",  matrix[coors[0]][coors[1]])
            visited[coorsString] = matrix[coors[0]][coors[1]]
            visitedCopy[coorsString] = matrix[coors[0]][coors[1]]
            
            
            ## checking y axis above
            if coors[0] != 0:
                if matrix[coors[0]-1][coors[1]] != 0:
                    coordinates = []
                    coordinates.append(coors[0]-1)
                    coordinates.append(coors[1])
                    stack.append(coordinates)
                
            ## checking y axis below
            if coors[0] != len(matrix) -1:
                if matrix[coors[0]+1][coors[1]] != 0:
                    #print("below", matrix[coors[0]+1][coors[1]])
                    coordinates = []
                    coordinates.append(coors[0]+1)
                    coordinates.append(coors[1])
                    stack.append(coordinates)
                
        ## checking x axis to the left
            if coors[1] != 0:
                if matrix[coors[0]][coors[1]-1] != 0:
                    #print("left", matrix[coors[0]][coors[1]-1])
                    coordinates = []
                    coordinates.append(coors[0])
                    coordinates.append(coors[1]-1)
                    stack.append(coordinates)
                
        ## checking x axis to the right
            if coors[1] != len(matrix[0]) -1:
                if matrix[coors[0]][coors[1]+1] != 0:
                    coordinates = []
                    coordinates.append(coors[0])
                    coordinates.append(coors[1]+1)
                    stack.append(coordinates)
            #print(stack)
    result_array = []
    result_array.append(visited)
    result_array.append(visitedCopy)
    #print("finished")
    #print(visitedCopy)
    return result_array
                
            
            
                    
                



def matrixElementsSum(matrix):
    ## so this is a graph traversel:
    
    ## going to use a stack store locations we still need to visit
    stack = []
    
    ## going use a dictionary to check track of visited rooms
    visited = {}
    rooms = {}
    
    ##Also we have to keep track of rooms that we have visited and the amount it costs
    roomsVisited = 0
    totalCost = 0
    
    ## we need to grab and index:
    for y in range(len(matrix)):
        for x in range(0, len(matrix[y])):
            ## now we need to check if the index is not a 0 meaing haunted
            if matrix[y][x] != 0:
                ## going to append the coordinates
                coordinates = []
                coordinates.append(y)
                coordinates.append(x)
                stack.append(coordinates)
                temp_visited = len(visited)
                result_array = travsGrid(matrix, y, x, visited, stack, roomsVisited, totalCost)
                visited = result_array[0]
                rooms = result_array[1]
                #print("rooms", rooms, "rooms len: ", len(rooms))
            if roomsVisited < len(rooms):
                roomsVisited = len(rooms)
                totalCost = 0
                for key in rooms:
                    totalCost += rooms.get(key)
    
    return totalCost
                    
            
