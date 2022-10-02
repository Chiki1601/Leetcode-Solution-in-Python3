class Solution:
    def deleteString(self, s: str) -> int:
        
        def findPairStringIndexes(s,i) :
            idxList = []
            for j in range(len(s)//2) :
                # think s[i:]
                if s[i:i+j+1] == s[i+j+1:i+2*j+2] :
                    idxList.append(j)
            return idxList
        
        # special case : number of operation is obvious
        if len(set(list(s))) == 1 : return len(s)

        # dynamic programming : because several truncate strategies are possible
        dp = [ 0 for _ in s ]
        i=0
        while i<len(s) :
            
            # list up possible pair case of s[i:] (index returns)
            idxList = findPairStringIndexes(s,i)
            # edge-case
            if i==0 and len(idxList)==0 : return 1
            
            # accumulate the number of operation
            for j in idxList :
                k = i+j
                dp[k+1] = max(dp[i],dp[k])+1   # number of operation
            
            # displace the pointer of s head
            while True :
                i+=1
                if i==len(s) : break
                if dp[i]!=0 : break
                
        return max(dp)+1
