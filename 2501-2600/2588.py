class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        M = DefaultDict(int)

        val = 0
        M[val] += 1

        for i in range(0, len(nums)):
            val = val ^ nums[i]
            M[val] += 1

        res = 0

        for m in M:
            res += (M[m] * (M[m]-1)) // 2
        
        return res
