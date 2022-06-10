class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSubL = 0
        if len(s) == 1:
            return 1
        if len(s) == 0:
            
            return 0
        if s == None:
            return 0
        
        for x in range(0, len(s)):
            longestSub = {}
            longestSub[s[x]] = 0
            for y in range(x+1, len(s)):
                
                if s[y] not in longestSub:
                    longestSub[s[y]] = 0
                    
                else:    
                    if len(longestSub) > maxSubL:
                        maxSubL = len(longestSub)
                    break
                
                if y == len(s) - 1:
                    if len(longestSub) > maxSubL:
                        maxSubL = len(longestSub)
                        break       
        return maxSubL
                    
