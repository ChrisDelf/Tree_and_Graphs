def evenDigitsOnly(n):
    ## since we must check every digit in the array we have to convert it into an array:
    ## first we convert the int into a string
    digitS = str(n)
    
    ## next we use list comprehension to convert into a array of ints
    
    digitI = [int(i) for i in digitS]
    
    ## now we can check if all the digits are even by iterrating through the array
    
    for j in range(len(digitI)):
        if digitI[j] % 2 != 0:
            return False
        
        
    return True

