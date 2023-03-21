class Solution:
    def beautifulSubsets(self, A: List[int], k: int) -> int:
        count = [Counter() for i in range(k)]
        for a in A:
            count[a % k][a] += 1
        res = 1
        for i in range(k):
            prev, dp0, dp1 = 0, 1, 0
            for a in sorted(count[i]):
                v = pow(2, count[i][a])
                if prev + k == a:
                    dp0, dp1 = dp0 + dp1, dp0 * (v - 1)
                else:
                    dp0, dp1 = dp0 + dp1, (dp0 + dp1) * (v - 1)
                prev = a
            res *= dp0 + dp1
        return res - 1
