class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        h, w = len(grid), len(grid[0])
        diff = [[0]*w for _ in range(h)]
        
        onesRow, zerosRow = [0]*h, [0]*h
        onesCol, zerosCol = [0]*w, [0]*w

        for i, row in enumerate(grid):
            onesRow[i] = sum(row)
            zerosRow[i] = len(row) - onesRow[i]

        for x in range(w):
            ones = 0
            for y in range(h):
                ones += grid[y][x]
            onesCol[x] = ones
            zerosCol[x] = h - onesCol[x]

        for y in range(h):
            for x in range(w):
                diff[y][x] = onesRow[y] + onesCol[x] - zerosRow[y] - zerosCol[x]

        return diff
