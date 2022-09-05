class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        current = 0 
        left = 0
        best = 0
        for right in range(N):
            while(current &nums[right])>0:
                current ^= nums[left]
                left += 1
                
            current |= nums[right]
            best = max(best,right - left + 1 )
        return best
