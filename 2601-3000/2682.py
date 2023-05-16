class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        start = 0
        sset = set()
        p = 1
        while start not in sset:
            sset.add(start)
            start += p*k
            start = start%n
            p += 1
        ans = []
        for i in range(n):
            if i not in sset:
                ans.append(i+1)
        return ans
            
        
