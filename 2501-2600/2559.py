class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res=[0]
        for word in words:
            if word[0] in 'aeiou' and word[-1] in 'aeiou':
                res.append(res[-1]+1)
            else:
                res.append(res[-1])


        ans=[]
        for l,r in queries:
            ans.append(res[r+1]-res[l])

        return ans
