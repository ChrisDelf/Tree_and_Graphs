def addBorder(picture):
    ## lets first get the height and width of this picture
    height = len(picture)
    width = len(picture[0])
    
    ## going to to create a new array to hold our modiftied array
    
    borderdP = []
    
    ## before we iterrate through any arrays lets check our input
    if picture == None or len(picture) == 0:
        return False
    
    ## we know that we will have a top and bottom border
    topBorder = ""
    bottomBorder = ""
    
    ## now lets fill those borders with * have to add the + 2 to account for the sides
    
    for i in range(0, width + 2):
        topBorder += "*"
        
    ## copy top border to bottom since they should be the same
    bottomBorder = topBorder
    
    ## now to tie this all together
    
    for i in range(0, height + 2):
        ## if we are at the first index we must added the top
        if i == 0:
            borderdP.append(topBorder)
        
        ## since this is the last row that we add we must break out of it
        else:
            
            for j in picture:
                tempString = "*"
                tempString += j
                tempString += "*"
                borderdP.append(tempString)
        
            borderdP.append(bottomBorder)
            break    
                
    return borderdP
