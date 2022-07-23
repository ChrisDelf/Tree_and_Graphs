#Solution 1
def plusOne(self, digits: List[int]) -> List[int]:
    
    # going to convert each int into a string to combine them 
    s = ""
    for d in digits:
        s += str(d)

    # now we will convert is back into an int 

    result  = str(int(s) + 1)
    
    arr = []
    for n in result:
        arr.append(int(n))

    return arr

#Solution 2
def plusOne(self, digits: List[int]) -> List[int]:
      # going to grab the last number from the array
    l_n = digits[-1] +1
    isCarrying = False
    if l_n < 10:
        digits[-1] = l_n
        return digits
    # we are going to have append to the array
    else:
        # digits.append(0)
        isCarrying = True
        for d in range(len(digits)-1,-1, -1):
            print(digits[d])
            if isCarrying == True:
                temp = digits[d] + 1
                digits[d] = temp
                if temp < 10:
                    isCarrying = False
                else:
                    digits[d] = 0
                    isCarrying = True
            
        #this case exist if we have 999999
        if isCarrying == True:
            digits[0] = 1
            digits.append(0)
            
    return digits
            



