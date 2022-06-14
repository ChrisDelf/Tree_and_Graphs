class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        s = set(words)
        words_dict = {}
        
        def recursion(word):
            if word not in s: return 0
            if word in words_dict:
                return words_dict[word]
            else:
                n = len(word)
                max_l = 0
                
                for i in range(0, n):
                    max_l = max(max_l, recursion(word[:i] + word[i+1:]) +1)
                words_dict[word] = max_l
                
            return max_l
            
        for w in words:
            recursion(w)
            
        return max(words_dict.values())
        
