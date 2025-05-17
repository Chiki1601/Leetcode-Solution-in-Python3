class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]

        for num in nums:
            count[num]+=1
        
        index = 0
        for color, freq in enumerate(count):
            for _ in range(freq):
                nums[index] = color
                index+=1 
