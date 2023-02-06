class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        a=list((''.join([str(nums[i]) for i in range(len(nums))])))
        return [int(a[i]) for i in range(len(a))]
