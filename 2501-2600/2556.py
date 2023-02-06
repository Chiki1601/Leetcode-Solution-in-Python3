class Solution:
    def isPossibleToCutPath(self, a: List[List[int]]) -> bool:
        m, n = len(a), len(a[0])
        vis1 = [[0 for i in range(n+2)] for j in range(m+2)]
        vis2 = [[0 for i in range(n+2)] for j in range(m+2)]
        vis1[0][1], vis2[m][n+1] = 1, 1
        cnt = [0] * (m+n-1)
        for i in range(1, m+1):
            for j in range(1, n+1):
                vis1[i][j] = a[i-1][j-1] and (vis1[i-1][j] or vis1[i][j-1])
        for i in range(m, 0, -1):
            for j in range(n, 0, -1):
                vis2[i][j] = a[i-1][j-1] and (vis2[i+1][j] or vis2[i][j+1])
                cnt[i+j-2] += vis1[i][j] and vis2[i][j]
        return any(cnt[i] < 2 for i in range(1, n + m - 2))
