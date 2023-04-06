class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res, temp = 0, "01"
        while len(temp) <= len(s):
            if temp in s: 
                res = len(temp)
            temp = '0' + temp + '1'
        return res
