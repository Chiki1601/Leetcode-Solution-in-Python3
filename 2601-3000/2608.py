class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        shortest = inf
        for i in range(n):
            dq, dist, parent = deque([i]), [inf] * n, [-1] * n
            dist[i] = 0
            while dq:
                node = dq.popleft()
                for kid in g.get(node, set()):
                    if dist[kid] == inf:
                        dist[kid] = dist[node] + 1
                        parent[kid] = node
                        dq.append(kid)
                    elif parent[kid] != node and parent[node] != kid:
                        shortest = min(shortest, dist[node] + dist[kid] + 1)
        return -1 if shortest == inf else shortest                
