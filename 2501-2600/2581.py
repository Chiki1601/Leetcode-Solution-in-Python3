class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges)
        if k == 0:
            return n + 1
        s = set()
        cnt = 0
        for i, j in guesses:
            if (j, i) not in s:
                s.add((i, j))
            else:
                s.remove((j, i))
                cnt += 1
        
        g = [[] for _ in range(n + 1)]
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)
        ans = 0
        q = deque([0])
        visited = [True] * (n + 1)
        visited[0] = False
        while q:
            i = q.popleft()
            for j in g[i]:
                if visited[j]:
                    q.append(j)
                    visited[j] = False
                    if (i, j) in s:
                        cnt += 1
        if cnt >= k:
            ans += 1
            
        q = deque([0])
        dp = [-1] * (n + 1)
        dp[0] = cnt
        while q:
            i = q.popleft()
            for j in g[i]:
                if dp[j] == -1:
                    q.append(j)
                    if (i, j) in s:
                        dp[j] = dp[i] - 1
                    elif (j, i) in s:
                        dp[j] = dp[i] + 1
                    else:
                        dp[j] = dp[i]
                    if dp[j] >= k:
                        ans += 1
        return ans
