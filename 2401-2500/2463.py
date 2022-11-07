class Solution:
    def minimumTotalDistance(self, A: List[int], B: List[List[int]]) -> int:
        n, m = len(A), len(B)
        dp = [inf] * (n + 1)
        dp[n] = 0
        A.sort()
        B.sort()
        for j in range(m-1,-1,-1):
            for i in range(n):
                cur = 0
                for k in range(1, min(B[j][1], n - i) + 1):
                    cur += abs(A[i + k - 1] - B[j][0])
                    dp[i] = min(dp[i], dp[i + k] + cur)
        return dp[0]        
