class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        return max(ceil(n / (i + 1)) for i, n in enumerate(accumulate(nums)))
