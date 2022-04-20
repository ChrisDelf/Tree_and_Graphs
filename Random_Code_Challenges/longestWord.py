import re

def solution(text):
    
    if text == None:
        return None
    if len(text) <= 0:
        return None
        
    words = re.split(";|,| |-|_ ", text)
    
  

    
    alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
    


    

    
    # now we can check for the lengths
    temp_word =""
    max = ""
    for w in words:
        temp_word = ""
        for l in w:
            if (l.lower()) in alphabet:
                
                temp_word += l
            else:
               
                break
               
       
        if len(temp_word) > len(max):
            
            max = temp_word
            
    return max
