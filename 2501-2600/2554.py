class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        c=0
        count=0
        banned=set(banned)
        for i in range(1,n+1):
            if i not in (banned):
                c+=i
                if c<=maxSum:
                    count+=1
                else:
                    count-=1
            if i>maxSum-c:
                break
        return count
