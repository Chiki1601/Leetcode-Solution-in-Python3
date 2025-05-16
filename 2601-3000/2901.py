class Solution:
    def hamming(self, s : str, t : str) -> bool:
        if len(s) != len(t):
            return False
        diff = 0
        for a, b in zip(s, t):
            if a != b:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n
        nxt = [-1] * n
        max_len = 0
        start = -1
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                if groups[i] != groups[j] and self.hamming(words[i], words[j]):
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        nxt[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                start = i
        res = []
        while start != -1:
            res.append(words[start])
            start = nxt[start]
        return res
