class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = []
        n = len(pref)
        if n == 0:
            return res
        elif n == 1:
            return [pref[0]]
        else:
            res.append(pref[0])
            for i in range(1,n):
                res.append(pref[i-1]^pref[i])
            return res
