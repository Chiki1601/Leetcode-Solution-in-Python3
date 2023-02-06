class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = []
        i = 0
        j = n
        while(i<j):
            x.append(nums[i])
            x.append(nums[n])
            i +=1
            n +=1
        return x
