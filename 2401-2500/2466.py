class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        dp, mod  = [1] + [0] * high, 1_000_000_007
        
        for k in range(1, high + 1):
            dp[k] = (dp[k - zero] + dp[k - one]) % mod
            
        return sum(dp[low:]) % mod
