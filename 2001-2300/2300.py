class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        N = len(potions)
        potions.sort()
        result = []
        for s in spells:
            target = math.ceil(success/s)
            idx = bisect.bisect_left(potions, target)
            result.append(N-idx)
        return result
        
