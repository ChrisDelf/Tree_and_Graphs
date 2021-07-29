def alphabeticShift(inputString):
    NUM = 31
    ## going to need to find the index position of the letters
    alphabetA = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    newString = ""
    for char in inputString:
        position = (ord(char) & NUM) - 1
        if position + 1 > 25:
            position = 0
        else:
            position += 1
        newString += alphabetA[position]
            
    
    return newString
     
