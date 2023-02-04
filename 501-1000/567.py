class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = [0] * 26
        for x in s1:
            cnt[ord(x) - ord('a')] += 1

        n1 = len(s1)
        n2 = len(s2)

        for i in range(n2 - n1 + 1):
            cnt2 = [0] * 26
            for j in range(i, i + n1):
                cnt2[ord(s2[j]) - ord('a')] += 1
            if cnt == cnt2:
                return True

        return False
