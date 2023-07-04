class Solution:
    def sumImbalanceNumbers(self, nums):
        n = len(nums)
        ans = 0
        for i in range(n):
            s = set()
            curr = 0
            for x in nums[i:]:
                if x in s: 
                    pass
                elif (x - 1 in s) and (x + 1 in s):
                    curr -= 1
                elif (x - 1 not in s) and (x + 1 not in s) and s:
                    curr += 1
                s.add(x)
                ans += curr
        return ans
