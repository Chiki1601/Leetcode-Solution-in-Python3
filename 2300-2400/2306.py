class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        mp = defaultdict(set)
        for i in ideas:
            mp[i[0]].add(i[1:])
            
        arr = list(mp.keys())
        ans, n = 0, len(arr)
        for i in range(n):
            for j in range(i+1, n):
                common = len(mp[arr[i]].intersection(mp[arr[j]]))
                ans += (len(mp[arr[i]])-common)*(len(mp[arr[j]])-common)*2
                
        return ans
