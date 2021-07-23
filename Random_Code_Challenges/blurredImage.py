def boxBlur(image):
    boxRows = len(image)
    boxCols = len(image[0])
    blurRows = boxRows - 2
    blurCols = boxCols - 2
    output = [[0 for x in range(blurCols)] for y in range(blurRows)] 
    currentValue = 0
    
    for i in range(0,blurRows):
        for j in range(0,blurCols):
            currentValue = image[i][j] + image[i][j+1] + image[i][j+2] + image[i+1][j] + image[i+1][j+1] + image[i+1][j+2] + image[i+2][j] + image[i+2][j+1] + image[i+2][j+2]
            currentValue = int(currentValue/9)
            output[i][j] = currentValue
        currentValue = 0
        
    return output
