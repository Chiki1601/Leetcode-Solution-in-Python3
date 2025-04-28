class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
      # prepare query
        for query in queries:
            if nums[query[0]] > nums[query[1]]:
                query[0], query[1] = query[1], query[0]
        query_pairs = [(nums[query[0]], nums[query[1]], i, query[0], query[1]) for i, query in enumerate(queries)]
        query_pairs.sort()

        # prepare furthest
        nums.sort()
        largest = max(nums)
        furthest = [i for i in range(largest + 1)]
        right = 0
        for num in nums:
            while right < n and nums[right] - num <= maxDiff:
                right += 1
            furthest[num] = nums[right - 1]
            
        @cache
        def dfs(frm, to):
            nxt = furthest[frm]
            if nxt >= to:
                return 1
            if nxt == frm:
                return -1
            rest = dfs(nxt, to)
            if rest == -1:
                return -1
            return 1 + rest        
  
        # calc ans
        ans = [0] * len(query_pairs)
        for frm, to, idx, node1, node2 in query_pairs:
            if  node1 != node2:
                ans[idx] = dfs(frm, to)             
        return ans
        
