
def isIPv4Address(inputString):
    modArray = inputString.split(".")
    singleInts = 0    
    if len(modArray) < 4:
        return False


    for i in range(0, len(modArray)):
        
        for char in modArray[i]:
            if char.isdigit() == False or char == '' or char == None:
                return False
    
        
        if len(modArray[i]) == 0:
            return False
            
        if len(modArray[i]) - 1 == 1:
            print("2", modArray[i][0])
            if int(modArray[i][0]) == 0:
                print("hello")
                return False
                
        if len(modArray[i]) - 1 == 2:
            if modArray[i][0] == 0:
                return False
            
        if len(modArray[i]) == 1:
            singleInts += 1
    
        if int(modArray[i]) > 255 or int(modArray[i]) < 0 :
            return False
            
    
    if singleInts == 5:
        return False
    
    return True
        
    


