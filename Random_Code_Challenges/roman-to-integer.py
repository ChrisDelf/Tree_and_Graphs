class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum_return = 0
        largest_roman = None
        is_skip = False
        
        
        
        for x in range(0 , len(s)):
            
            if is_skip == False:
                
                
                current_r = s[x]


                if x+1  <= len(s) - 1:

                    next_r = s[x + 1]


                else:
                    next_r = None
                ## need this check just incase we encounter a non roman numeral
                if current_r in romans:
                    ## we have to check if the numeral after it is largeer or smaller
                    current_r = romans[current_r]

                    if next_r != None and next_r in romans:
                       
                        next_r = romans[next_r]
                        
                        print("Current :", current_r, "Next :", next_r)
                        if current_r >= next_r:

                            sum_return += romans[s[x]]
                            is_skip = False
                        else:


                            sum_return += (next_r - current_r)
                            
                            is_skip = True


                    else:
                        sum_return += current_r



                    





                else:
                    return False
            else:
                is_skip = False 
        return sum_return
