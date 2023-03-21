from sortedcontainers import *

class Solution:
    def findScore(self, nums: List[int]) -> int:
        val_index, score = SortedSet(), 0
        for i, num in enumerate(nums):
            val_index.add((num, i))
        while len(val_index) > 0:
            key, idx = val_index.pop(0)
            score += key
            for neighbor_index in idx - 1, idx + 1:    
                if 0 <= neighbor_index < len(nums):
                    val_index.discard((nums[neighbor_index], neighbor_index))
        return score
