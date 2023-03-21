class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        dicts = defaultdict(list)
        m, n = len(grid), len(grid[0])
        seen = set()
        for i in range(m):
            for j in range(n):
                dicts[grid[i][j]] = [i,j]
                seen.add((i,j))
        if len(dicts) != m*n or len(seen) != m*n:
            return False
        else:
            for i in range(m*n-1):
                sx, sy = dicts[i]
                if i == 0 and (sx != 0 or sy != 0): return False
                tx, ty = dicts[i+1]
                if (abs(sx - tx) == 1 and abs(sy - ty) == 2) or \
                   (abs(sy - ty) == 1 and abs(sx - tx) == 2):
                    continue
                else:
                    return False
            return True
