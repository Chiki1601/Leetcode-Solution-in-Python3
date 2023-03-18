class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        visited = [False] * 2001
        for a, b, d in sorted(tasks, key=lambda x: x[1]):
            d -= sum(map(lambda x: visited[x], range(a, b + 1)))
            for i in range(b, a - 1, -1):
                if d <= 0:
                    break
                d -= not visited[i]
                visited[i] = True
        return sum(visited)
