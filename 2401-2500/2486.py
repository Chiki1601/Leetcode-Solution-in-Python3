class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        #Reversed in order to pop the first character each time
        t = list(t)[::-1]
        
        for c in s:
            #t is already a subsequence
            if not t: return 0
            #pop t if c == "first character" of t 
            if c == t[-1]: t.pop()
                
        #Return the left over t length
        return len(t)           
