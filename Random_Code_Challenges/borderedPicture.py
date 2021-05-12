def addBorder(picture):
    ## to add a border we must know the lenght and height of the 2d grid
    height = len(picture)
    length = len(picture[0])
    
    ## for the border of the height we must add addition rows
    ## for the length we must additional columns
    
    borderedP = []
    topRow = []
    bottomRow = []
    
    ##going to create the first and last rows
    for i in range(0, len(length + 2)):
        topRow.append("*")
        bottomRow.append("*")
    ## going to append our rows
    for j in range(0,len(height + 2)):
        ## adding the top border
        if j == 0:
            borderedP.append(topRow)
        elif j == len(height + 2):
            borderdP.append(bottomRow)
        else:
            tempArray = []
            for x in range(0,len(length + 2))
            
                if x == 0:
                    tempArray.append("*")
                elif x == len(length + 2):
                    tempArray.append("*")
                else:
                    
        
        
        
            
        
        
    if len(picture) <= 0:
        break
    
    ## now for us to append the toprow
    borderedP.append(topRow)
    
    
