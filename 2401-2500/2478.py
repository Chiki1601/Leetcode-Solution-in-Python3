class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        n, primes, mod = len(s), set('2357'), (10 ** 9) + 7
        @cache
        def dp(i, at_start, k):
            if i == n: return int(k == 0)
            if i > n or k == 0 or s[i] not in primes and at_start: return 0
            if s[i] in primes:
                if at_start: return dp(i + minLength - 1, False, k)
                else: return dp(i + 1, False, k)
            return (dp(i + 1, True, k - 1) + dp(i + 1, False, k)) % mod
        return dp(0, True, k)
