class Solution:
    def maximizeWin(self, A, k):
        dp = [0] * (len(A) + 1)
        res = j = 0
        for i, a in enumerate(A):
            while A[j] < A[i] - k: j += 1
            dp[i + 1] = max(dp[i], i - j + 1)
            res = max(res, i - j + 1 + dp[j])
        return res
