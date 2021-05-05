
def reverseInParentheses(inputString):
    ## going to store the parentheses in a stack
    stack = []
    i_start = []
    i_end = []
    outputString = []
    i = 0
    pCounter = 0
    counter = 0
    while len(outputString) < len(inputString) and i <= len(inputString) - 1:
        ## once we encounter a parenthese  it goes into the stack
        print(i)
        if inputString[i] == "(":
            stack.append(inputString[i])
            i_start.append(i)
        
        if inputString[i] == ")":
            closingP = stack.pop() 
            if closingP != "(":
                return False;
            i_end.append(i)
                
        if len(stack) > 0:
            outputString.append(inputString[i]) 

               
        i += 1
        
    if len(stack) > 0:
        return False;
    print("starting index", i_start, "ending_index", i_end);

