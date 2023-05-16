class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        
        #we try 0 and 1 as potential first elements
        for first in [0,1]:
            original=first
            for result in derived[:-1]:
                #we apply the reverse operation as shown in the pictures
                original=original^result
            #finally, we check if the validity condtion is true
            if original^first==derived[-1]:
                return True
        return False
        
