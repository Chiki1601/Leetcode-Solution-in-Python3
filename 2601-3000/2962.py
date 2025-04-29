class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        count = Counter()
        maxVal = max(nums)
        ans, n = 0, len(nums)
        while j < n:
            count[nums[j]] += 1
            while count[maxVal] == k:
                count[nums[i]] -= 1
                i += 1
            ans += i
            j += 1
        return ans
