class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        
        cnt, prv, nxt = 0, 0, len(nums)
        
        for _, cur in Counter(nums).items(): 
            nxt -= cur                         # update sum of remaining frequencies
            cnt += prv * cur * nxt             # number of tiples for each unique number
            prv += cur                         # update sum of seen frequencies
        return cnt
