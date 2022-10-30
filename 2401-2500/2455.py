class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        nums = [n for n in nums if not n%6]
        
        return sum(nums)//len(nums) if nums else 0
