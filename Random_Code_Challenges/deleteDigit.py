def solution(n):
    # we just have to delete the smallest int
    inputS = str(n)
    min = None
    min2 = None
    max = None
    inputL = len(inputS)
    
  
    
    #need to check for second to last number
   
    
    for x in range(0 , inputL):
          
        if min == None:
            min = int(inputS[x])
          
        if max == None:
            max = int(inputS[x])
          
            
        if max < int(inputS[x]):
            max = int(inputS[x])
          
            
        if min > int(inputS[x]):
            min2 = min
            min = int(inputS[x])
         
            
        
        
        
             
    if inputL > 3:
    
        if min == int(inputS[inputL-1]) and max == int(inputS[inputL-2]):
            result = inputS.replace(str(min2),"", 1)
            return int(result)  
            
        
    
    result = inputS.replace(str(min),"", 1)
        
    
    
    return int(result)        

 
             

