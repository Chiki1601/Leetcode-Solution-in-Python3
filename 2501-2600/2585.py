class Solution:
    def waysToReachTarget(self, target, T, mod = 1000000007):
        return (lambda dp: dp(dp, 0, target))(lru_cache(maxsize=None)(lambda f, i, t: 1 if t == 0 else 0 if i >= len(T) or t < 0 else sum(f(f, i+1, t-j*T[i][1]) for j in range(T[i][0]+1)) % mod))
