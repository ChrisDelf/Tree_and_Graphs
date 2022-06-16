import math
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result_s = ""
        
        result_len = 0
        
        for i in range(len(s)):
            # odd length
            left_p, right_p = i,i
            
            while left_p >= 0 and right_p < len(s) and s[left_p] == s[right_p]:
                if (right_p - left_p + 1) > result_len:
                    result_s = s[left_p:right_p + 1]
                    result_len = right_p - left_p + 1
                    
                left_p -= 1
                right_p += 1
                
            # even length
            left_p, right_p = i,i +1
            while left_p >= 0 and right_p < len(s) and s[left_p] == s[right_p]:
                 if (right_p - left_p + 1) > result_len:
                    result_s = s[left_p:right_p + 1]
                    result_len = right_p - left_p + 1
                    
                 left_p -= 1
                 right_p += 1
                
        return result_s
                
