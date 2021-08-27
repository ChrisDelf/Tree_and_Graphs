def bishopAndPawn(bishop, pawn):
    if bishop == pawn:
        return False;
    if bishop[0] == pawn[0]:
        return False;
    if bishop[1] == pawn[1]:
        return False;
    ## we have to check 4 vertices 
    
    topLeft= [-1,+1]
    bottomLeft= [-1,-1]
    topRight= [+1, +1]
    bottomRight= [+1, -1]
    
    length = 7
    height = 7
    
    index = 0
    
    positions = {"a":0,"b":1,"c":2,"d":3, "e":4, "f":5, "g":6, "h":7}
    newBishop = []
    newPawn = []
    if bishop[0] in positions:
        newBishop.append(positions[bishop[0]])
        newBishop.append(int(bishop[1]))
    if pawn[0] in positions:
        newPawn.append(positions[pawn[0]])
        newPawn.append(int(pawn[1]))
        

    
    ## now that we have converted positions into ints we can look at what direction we need to go
    ## if the x position is greater than the bishop we go right else we go left
    ## same can be done for the up or down.
    isLeft = True
    increment = []
    if newBishop[0] > newPawn[0]:
        increment.append(-1)
        isLeft = True
    else:
        increment.append(+1)
        isLeft = False
    
    if newBishop[1] > newPawn[1]:
        increment.append(-1)
    else:
        increment.append(+1)
        

    
    
    
    if isLeft == False:
        tempA = [newBishop[0], newBishop[1]]
        for i in range(newBishop[0], newPawn[0] + 1):
        
            tempA[0] = tempA[0] + increment[0]
            tempA[1] = tempA[1] + increment[1]
        
            if newPawn[0] == tempA[0]:
                if newPawn[1] == tempA[1]:
                    return True;
                else:
                    return False;
    else:
        tempA = [newBishop[0], newBishop[1]]

        for j in range( newBishop[0] +1, newPawn[0] ,-1):
            
            tempA[0] = tempA[0] + increment[0]
            tempA[1] = tempA[1] + increment[1]
        
            if newPawn[0] == tempA[0]:
                if newPawn[1] == tempA[1]:
                    return True;
                else:
                    return False;    
   
