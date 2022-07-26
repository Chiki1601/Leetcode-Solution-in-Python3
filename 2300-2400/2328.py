class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        final=0
        mod=10**9+7 
        stack=[]
        n=len(grid)
        m=len(grid[0])
        visited=defaultdict(bool)
        def toposort(v):
            visited[v]=True 
            neighbours=[(v[0]+1,v[1]),(v[0]-1,v[1]),(v[0],v[1]+1),(v[0],v[1]-1)]
            for i,j in neighbours:
                if 0<=i<n and 0<=j<m and visited[(i,j)]==False and grid[i][j]>grid[v[0]][v[1]]:
                    toposort((i,j))
            stack.append(v)
        for i in range(n):
            for j in range(m):
                if visited[(i,j)]==False:
                    toposort((i,j))
        stack.reverse()
        dp=defaultdict(int)
        for i in range(len(stack)):
            x,y=stack[i]
            v=(x,y)
            dp[(x,y)]+=1
            neighbours=[(v[0]+1,v[1]),(v[0]-1,v[1]),(v[0],v[1]+1),(v[0],v[1]-1)]
            for i,j in neighbours:
                if 0<=i<n and 0<=j<m and grid[i][j]>grid[v[0]][v[1]]:
                    dp[(i,j)]+=dp[(x,y)]
                    dp[(i,j)]%=mod
            final+=dp[(x,y)]
            final%=mod
        return final
            
