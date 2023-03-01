class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        l,r=0,len(nums)//2
        while r<len(nums) and l<len(nums)//2:
            if 2*nums[l]<=nums[r]: l+=1
            r+=1
        return l*2
