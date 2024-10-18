class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        def lis(arr):
            # greedy O(n log n) LIS approach
            # We sort by (x, -y), and track only the y coordinate.
            # Because of this sorting, for a given (x,y) if y > lis[-1]
            # then it is necessarily true that x is strictly larger than the previous x-coordinate.
            arr.sort(key=lambda tup: (tup[0], -tup[1]))
            res = []
            for x,y in arr:
                if not res or y > res[-1]:
                    res.append(y)
                else:
                    i = bisect_left(res, y)
                    res[i] = y
            
            return len(res)
        
        mx, my = coordinates[k]
        coordinates.sort()
        
        # smaller elements
        left = [(x,y) for x,y in coordinates if x < mx and y < my]
        
        # larger elements
        right = [(x,y) for x,y in coordinates if x > mx and y > my]

        return 1 + lis(left) + lis(right)
        
