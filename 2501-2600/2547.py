class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        
        @cache
        def dp(i):
            if i == len(nums):
                return 0

            m = float('inf')
            
            hm = defaultdict(int)
            count = 0
            for j in range(i,len(nums)):
                hm[nums[j]] += 1
                
                if hm[nums[j]] > 2:
                    count += 1
                
                elif hm[nums[j]] == 2:
                    count += 2
                
                cal = k + count

                m = min( cal + dp(j+1)  , m )
                
            return m

        return dp(0) 
