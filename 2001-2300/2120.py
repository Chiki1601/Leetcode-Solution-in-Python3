class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        result = []

        counter = 0
        for i in range(len(s)):
            if counter:
                result.append(counter)
            cell = list(startPos)
            counter = 0

            for j in range(i, len(s)):
                if s[j] == 'U':
                    cell[0] -= 1
                elif s[j] == 'D':
                    cell[0] += 1
                elif s[j] == 'L':
                    cell[1] -= 1
                elif s[j] == 'R':
                    cell[1] += 1

                if cell[0] >= n or cell[0] < 0 or cell[1] >= n or cell[1] < 0:
                    result.append(counter)
                    counter = 0
                    break
                else:
                    counter += 1
        if counter:
            result.append(counter)

        return result
      
