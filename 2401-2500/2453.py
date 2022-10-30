class Solution:

    def destroyTargets(self, nums: List[int], space: int) -> int:
        dct = dict() 
        mx = 0 # maximum of destroyed targets
        
        for num in nums:
            x = num % space # if the numbers have the same remainder after division by space, 
                            # then they can be presented in the form : nums[i] + c * space
            if x not in dct:
                dct[x] = (1, num)
            else:
                dct[x] = (dct[x][0] + 1, min(dct[x][1], num)) # we always keep the minimum nums[i] for all remainders 
                
            mx = max(mx, dct[x][0])
            
        res = float("inf")
        for val in dct.values(): #we just go through all the values and find the result
            if val[0] == mx:
                res = min(res, val[1])
        
        return res
