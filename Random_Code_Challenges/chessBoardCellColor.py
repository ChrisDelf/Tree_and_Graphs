def chessBoardCellColor(cell1, cell2):
    ## going to generate a dictionary that has all the positions
    chessBoard = {}
    
    letters = ["a", "b", "c","d", "e", "f", "g", "h"]
    numbers = [1,2,3,4,5,6,7,8]
    alterR  = True
    for i in range(len(letters)):
        
        for j in range(len(numbers)):
            positionM = letters[i].upper() + str(numbers[j])
            
            if positionM not in chessBoard:
                chessBoard[positionM] = 0
                if alterR == True:
                    chessBoard[positionM] = "black"
                    if len(numbers)-1 > j:
                        alterR = False
                else: 
                    chessBoard[positionM] = "white"
                    if len(numbers)-1 > j:
                        alterR = True
                
    
    if chessBoard[cell1] == chessBoard[cell2]:
        return True
    else:
        return False

