class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        p=0
        sum=nums[0]+nums[1]
        for x in nums[2:]:
            if sum>x:
                p=sum+x
            sum+=x
        if p==0: return -1
        else: return p
        
        
