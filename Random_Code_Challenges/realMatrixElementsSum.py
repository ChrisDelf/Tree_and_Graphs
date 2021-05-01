
def matrixElementsSum(matrix):
    roomCost = 0
    visitedRooms = 0
    for i in range(len(matrix[0])):
        if matrix[0][i] != 0:
            roomCost += matrix[0][i]
            visitedRooms += 1
        ## so if the room is not haunt then we can check the rooms below it
            for j in range(1, len(matrix)):
                if matrix[j][i] != 0:
                    roomCost += matrix[j][i]
                    visitedRooms += 1
                else:
                    break
    
    
    return roomCost
