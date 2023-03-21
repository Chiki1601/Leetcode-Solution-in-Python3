class Solution:
    def findSmallestInteger(self, A: List[int], v: int) -> int:
        n = len(A)
        m = min(n, v)
        dp = [0] * m
        for i in A:
            if i % v < m:  
                dp[i % v] += 1
        for i in range(n):
            if i % v >= n or dp[i % v] == 0: return i 
            dp[i % v] -= 1
        return n
