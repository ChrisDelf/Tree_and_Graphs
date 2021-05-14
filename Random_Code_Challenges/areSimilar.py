def areSimilar(a, b):
    ## going to need a pointer that advances head of the index
    swapP = 0
    laggingP = 0
    ## if the lengths don't match then we return false
    if len(a) > len(b):
        return False;
    ## going to need a swap counter
    aCounter = 0
    bCounter = 0
    
    for i in range(len(a)):
        swapP = i + 1
        laggingP = i - 1
        
        
        if swapP >=len(a):
            if a[i] != b[i] and a[i] != b[laggingP]:
                return False;
                
        if laggingP >= 0:
            if a[i] != b[i] and a[i] != b[swapP] and a[i] != b[laggingP]:
                return False;
        else:
            if a[i] != b[i] and a[i] != b[swapP]:
                return False;
    
    return True;
        

