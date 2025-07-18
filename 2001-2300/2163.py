import heapq
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        total_len = 3 * n

        left_sum = [0] * total_len
        max_heap = []
        curr_sum = 0

        for i in range(total_len):
            heapq.heappush(max_heap, -nums[i])
            curr_sum += nums[i]

            if len(max_heap) > n:
                curr_sum += heapq.heappop(max_heap)

            if i >= n - 1:
                left_sum[i] = curr_sum

        right_sum = [0] * total_len
        min_heap = []
        curr_sum = 0

        for i in range(total_len - 1, -1, -1):
            heapq.heappush(min_heap, nums[i])
            curr_sum += nums[i]

            if len(min_heap) > n:
                curr_sum -= heapq.heappop(min_heap)

            if i <= 2 * n:
                right_sum[i] = curr_sum

        res = float('inf')
        for i in range(n - 1, 2 * n):
            res = min(res, left_sum[i] - right_sum[i + 1])

        return res
