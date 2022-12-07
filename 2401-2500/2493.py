class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size
        self.connected = size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.connected -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        ind = [0]*n
        uf = UnionFind(n)
        for x,y in edges:
            graph[x-1].append(y-1)
            graph[y-1].append(x-1)
            ind[x-1] += 1
            ind[y-1] += 1
            uf.union(x-1,y-1)
            
        
        order = defaultdict(list)
        for i in range(len(ind)):
            order[uf.find(i)].append(i)
                
        def bfs(start):
            
            q = deque()
            q.append((start,1))
            layers = defaultdict(int)
            layers[start] = 1
            ans = -1
            
            while q:
                for _ in range(len(q)):
                    node, layer = q.popleft()
                    if layer > ans:
                        ans = layer
                    for x in graph[node]:
                        if x not in layers:
                            q.append((x, layer+1))
                            layers[x] = layer+1
                        if layers[node] == layers[x]:
                            return -1
            return ans
        
        ans = 0
        
        for x in order:
            tmp = -1
            for startNode in order[x]:
                tmp = max(tmp, bfs(startNode))
            if tmp == -1:
                return -1
            ans += tmp
            
        return ans
  # Time O((m+n)^2) space O(n)
