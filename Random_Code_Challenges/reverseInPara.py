
def reverseInParentheses(inputString): 
## going to use a stack to keep track of all the parentheses
    stack = []
## going to need to have a start and end pointer to know what sections to reverse
    i_start = []
    i_end = []
    
    for i in range(0, len(inputString)):
        ## we encounter a opening parentheses add it to the stack
        if inputString[i] == "(":
            stack.append(inputString[i])
            i_start.append(i)
        
        if inputString[i] == ")":
            openingP = stack.pop()
            if openingP == "(":
                ## we are good to go.
                i_end.append(i)
            
            else:
                ## this closing parentheses does not have a opeing to complement it
                return False
    
    ## now since we have our pointers stored we need to iterrate through them to reverse the letters.
    outputS = inputString
    ## start and end pointers
    start = 0
    end = 0
    
    isClean = True
    
    while len(i_start) > 0:
        start = i_start.pop()
        end = i_end.pop()
        
        ## we need to hand a case in which we have a closing "))"
        if inputString[end] == ")" and inputString[end-1] == ")":
            outputS = outputS[:start] + outputS[start+1:end][::-1] + outputS[end:]
            isClean = False
        else:
            outputS = outputS[:start] + outputS[start+1:end][::-1] + outputS[end+1:]
            
    result_string = ""
    
    if isClean == False:
        for x in range(0, len(outputS)):
            if outputS[x] != "(" and outputS[x] != ")":
                result_string += outputS[x]
            
        return result_string
    else:
        return outputS
     
        
