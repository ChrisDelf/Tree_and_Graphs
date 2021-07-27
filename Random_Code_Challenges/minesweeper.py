def minesweeper(matrix):
    ## going to create the new matrix
    ## going to need to know the demisions of our matrix so height and width
    outputM = []
    print(len(matrix))
    # now we must iterrate through the input to create our output matrix
    for i in range(0,len(matrix)):
        ## each time we go to a new row we must create a new array
        newRow = []
       
        for j in range(0,len(matrix[i])):
            mineC = 0
            print(i, j)
            ## top
            if 0 <= i - 1 and matrix[i-1][j] == True:
                mineC += 1
            ## bottom
            if len(matrix)-1 >= i + 1 and matrix[i+1][j] == True:
                
                mineC += 1
            ## left
            if 0 <= j - 1 and matrix[i][j - 1] == True:
              
                mineC += 1
            ## right
                
            if len(matrix[i])-1 >= j + 1 and matrix[i][j + 1] == True:
                
                mineC += 1
                
            ## now we check diagonals
            ## top left
            if 0 <= i - 1 and 0 <= j - 1 and matrix[i-1][j-1] == True:
                mineC += 1
            ## top right
            if 0 <= i - 1 and len(matrix[i])-1 >= j + 1 and matrix[i-1][j+1] == True:
                mineC += 1
            ## bottom left 
            if len(matrix)-1 >= i + 1 and 0 <= j - 1 and matrix[i+1][j-1] == True:
               
                mineC += 1
            ## bottom right
            if len(matrix)-1 >= i + 1 and len(matrix[i])-1 >= j + 1 and matrix[i+1][j+1] == True:
                mineC += 1
            
            newRow.append(mineC)
            
        outputM.append(newRow)
        
    return outputM 
                
