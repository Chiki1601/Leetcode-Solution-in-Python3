mx = 10**6
spf = [i for i in range(mx+1)]
for i in range(2,int(math.sqrt(mx))+1):
    if spf[i]==i:
        for j in range(i*i,mx+1,i):
            spf[j]=min(spf[j],i)
def getPrimeFactors(x):
    while x!=1:
        yield spf[x]
        x//=spf[x]
class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        fac_idx = defaultdict(int)
        for i,v in enumerate(nums):
            for fac in getPrimeFactors(v):
                fac_idx[fac] = i
        right_most = 0
        for i in range(len(nums)-1):
            for fac in getPrimeFactors(nums[i]):
                right_most = max(right_most,fac_idx[fac])
            if right_most==i:
                return i
        return -1
