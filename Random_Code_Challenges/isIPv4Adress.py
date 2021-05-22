def isIPv4Address(inputString):
    modArray = inputString.split(".")
    
    if len(modArray) < 4:
        return False
    

    for i in range(0, len(modArray)):
        
        for char in modArray[i]:
            print(char)
            if char.isdigit() == False or char == '' or char == None:
                return False

        if len(modArray[i]) == 0:
            return False  
        if int(modArray[i]) > 255 or int(modArray[i]) < 0 :
            return False
            
    
    
    return True
        
