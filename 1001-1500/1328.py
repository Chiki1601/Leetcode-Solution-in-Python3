class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ''
        
        pal = list(palindrome)
        mid = len(pal) // 2 
        if len(pal) % 2: mid -= 1 # odd length palindrome case
        
        for i in range(mid + 1):
            if pal[i] != 'a':
                pal[i] = 'a'
                return ('').join(pal)
        
        if pal[-1] != 'a':
            pal[-1] = 'a'
            return ('').join(pal)
        
        pal[-1] = 'b'
        return ('').join(pal)
