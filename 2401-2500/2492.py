class Solution:
    def minScore(self, n: int, a: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for i, j, d in a:
            g[i].append((j, d))
            g[j].append((i, d))
        ans = 10000
        vis = set()
        dq = [1]
        while dq:
            node = dq.pop()
            vis.add(node)
            for i, d in g[node]:
                if i not in vis:
                    dq.append(i)
                ans = min(ans, d)
        return ans
