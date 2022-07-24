class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        columns = list(range(1, 9))
        flag = True
        mapping = {}
        for row in rows:
            flag = not flag
            for col in columns:
                index = row + str(col)
                mapping[index] = flag
                flag = not flag
        return mapping[coordinates]
