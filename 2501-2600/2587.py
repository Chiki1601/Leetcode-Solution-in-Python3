class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)
        max_score = 0
        for i in range(1, len(prefix_sums)):
            if prefix_sums[i] > 0:
                max_score = i
        return max_score
