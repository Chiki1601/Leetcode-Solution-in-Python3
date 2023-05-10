ans = 0
def dfs(n, cost, i):
    global ans
    if(i > n):
        return 0
    leftCost = dfs(n,cost,2 * i);
    rightCost = dfs(n,cost,2 * i + 1);
    ans += abs(leftCost - rightCost);
    return max(leftCost,rightCost) + cost[i - 1];
    
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        global ans
        ans = 0
        dfs(n,cost,1)
        return ans
        
