class Solution:
    def componentValue(self, A: List[int], E: List[List[int]]) -> int:
        ma, ss, n = max(A), sum(A), len(A)
        if n == 1: return 0
        G = collections.defaultdict(set)
        degree = [0] * n
        for a, b in E:
            degree[a] += 1
            degree[b] += 1
            G[a].add(b)
            G[b].add(a)
            
        def bfs(target):
            V, deg = A[:], degree[:]
            dq = collections.deque([i for i, d in enumerate(degree) if d == 1])
            
            while dq:
                ci = dq.popleft()
                if deg[ci] == 0: continue
                deg[ci] = 0
				
				# Edge case: if current value is target, don't push value to its parent.
                if V[ci] == target:
                    for nxt in G[ci]:
                        deg[nxt] -= 1
                        if deg[nxt] == 0: # Edge case: if its 'parent' is the last node, check if its value equals target.
                            return V[nxt] == target
                        elif deg[nxt] == 1:
                            dq.append(nxt)
                else: # Otherwise, we need to push its value to its parent.
                    for nxt in G[ci]:
                        if deg[nxt] > 0:
                            deg[nxt] -= 1
                            V[nxt] += V[ci]
                            if deg[nxt] == 0: # Edge case: if its the last node, check if its value equals target.
                                return V[nxt] == target
                            elif deg[nxt] == 1:
                                dq.append(nxt)     
           
        for cand in range(1, ss):
            if ss % cand == 0 and bfs(cand):
                return ss // cand - 1
        return 0
