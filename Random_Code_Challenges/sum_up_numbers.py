import re

def solution(inputString):
    
    intDic = {0:'0', 1: '1', 2: '2', 3: '3',4: '4',5: '5',6: '6',7: '7', 8: '8',9: '9'}
    
    result = re.split('(\d+)', inputString)
    
    the_sum = 0
    
    for i in range(0, len(result) - 1):
        number = result[i]
        # before we convert the element from a string to an integer we need to make sure it a int
        if number.isdigit() == True:
             the_sum += int(number)
        
        
    return the_sum
