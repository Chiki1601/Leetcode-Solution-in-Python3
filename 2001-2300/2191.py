class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        seen = []
    
        for num in nums:
            newWord = ""
            for char in str(num):
                newWord = newWord + str(mapping[int(char)])
            seen.append(int(newWord))  
            
     
        final = list(zip(nums, seen))
    
        final = sorted(final, key = lambda x:x[1])
    
        return [tup[0] for tup in final]
