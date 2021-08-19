def longestDigitsPrefix(inputString):
    mLength = 0
    largestString = ""
    isPrefix = True
 
    if inputString[0].isnumeric() == False:
        return ""
        
    for i in range(0, len(inputString)):
        tempString = ""
        if inputString[i].isnumeric():
            ## then we go into another loop

            if largestString == None:
                largestString = tempString
            
            for i in range(i, len(inputString)):
                if inputString[i].isnumeric() == False:
                    if inputString[i] == " ":
                        return "" 
                    if inputString[i] == ")":
                        return ""
                    break
                else:
                    tempString += inputString[i]
            
        if len(tempString) > len(largestString):
            largestString = tempString
            return largestString
  

