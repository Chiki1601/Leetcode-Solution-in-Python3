class Solution:
    def dividePlayers(self, S: List[int]) -> int:
        S.sort()
        n = len(S)
        s = S[0] + S[-1]
        total = 0
        for i in range(n // 2):
            if s != S[i] + S[n - i - 1]:
                return -1
            total += S[i] * S[n - i - 1]
            
        return total
