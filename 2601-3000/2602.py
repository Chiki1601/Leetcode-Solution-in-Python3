class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [0] + list(accumulate(nums))
        for x in queries:
            i = bisect_left(nums, x)
            yield x * (2 * i - len(nums)) + prefix[-1] - 2 * prefix[i]
