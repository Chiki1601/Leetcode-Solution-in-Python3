class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        n = len(nums)
        odd_inds = n >> 1
        even_inds = n - odd_inds
        if not (-12 * odd_inds <= k <= 12 * even_inds):
            return -1
        
        odd_sums = collections.defaultdict(set)
        even_sums = collections.defaultdict(set)
        
        for val in nums:
            new_odd_sums = collections.defaultdict(set)
            for curr in even_sums:
                new_odd_sums[curr + val] = {i * val for i in even_sums[curr] if i * val <= limit}
                if val == 0:
                    new_odd_sums[curr + val].add(0)
            new_even_sums = collections.defaultdict(set)
            for curr in odd_sums:
                new_even_sums[curr - val] = {i * val for i in odd_sums[curr] if i * val <= limit}
                if val == 0:
                    new_even_sums[curr + val].add(0)
            
            for i in new_odd_sums:
                odd_sums[i].update(new_odd_sums[i])
            for i in new_even_sums:
                even_sums[i].update(new_even_sums[i])
            
            if val <= limit:
                odd_sums[val].add(val)
        print(odd_sums)
        print(even_sums)
        #for i in range(-12 * odd_inds, 12 * even_inds + 1):
        #    print(i, max(max(odd_sums[i]) if len(odd_sums[i]) else -1, max(even_sums[i]) if len(even_sums[i]) else -1))
        
        ans = -1
        if len(odd_sums[k]):
            ans = max(ans, max(odd_sums[k]))
        if len(even_sums[k]):
            ans = max(ans, max(even_sums[k]))
        
        return ans
    
