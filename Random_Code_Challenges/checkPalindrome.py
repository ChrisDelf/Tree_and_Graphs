def checkPalindrome(inputString):
  
    is_even = False;
    midpoint = math.floor(len(inputString) / 2)
    
    if len(inputString) <= 0:
        return True;
    ## going to use a modulo to find the mid-point "%"
    if len(inputString) % 2 == 0:
        is_even = True;
    ## since its true we can compare two indexs that are next to each other to see if they are the same
    if (inputString[int(midpoint-1)] != inputString[int(midpoint)]) & (is_even == True):
        print("hellp")
        return False;
    
    ## going to go with a double pointer approach:
    start_p = 0
    end_p = len(inputString) - 1
    
    print(end_p)
    ## now to iterrate 
    for i in range(0, midpoint - 1):
      if  inputString[i] != inputString[end_p]:
        print(start_p, end_p)
        return False;

      end_p -= 1
      

    return True 
