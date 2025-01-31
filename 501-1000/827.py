class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        stack = []
        tag, area_dict = 2, {}

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area = 0
                    stack.append((i, j))
                    grid[i][j] = tag
                    while stack:
                        x, y = stack.pop()
                        area += 1
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            xx, yy = x + dx, y + dy
                            if 0 <= xx < n and 0 <= yy < n and grid[xx][yy] == 1:
                                stack.append((xx, yy))
                                grid[xx][yy] = tag
                    area_dict[tag] = area
                    tag += 1

        if not area_dict:  # if no island
            return 1
            
        max_area = max(area_dict.values())  # if no ocean
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    area = 1
                    islands = set()
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ii, jj = i + di, j + dj
                        if 0 <= ii < n and 0 <= jj < n and grid[ii][jj] != 0:
                            islands.add(grid[ii][jj])
                    for island in islands:
                        area += area_dict[island]
                    max_area = max(max_area, area)

        return max_area
