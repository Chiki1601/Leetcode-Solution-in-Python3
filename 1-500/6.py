class Solution:
    def convert(self, s, numRows):
        i,diagonal = 0, False
        d = {j:'' for j in range(0, numRows)}
        while i<len(s):
            # linear part: from top row to bottom
            if diagonal == False:
                for j in range(0, numRows):
                    d[j] += s[i]
                    i += 1
                    if i>=len(s):
                        break
            # diagonal part: from bottom row to top, skipping first and last rows
            else:
                for j in range(numRows-1, -1, -1):
                    if j==0 or j==(numRows-1):
                        continue
                    else:
                        d[j] += s[i]
                        i += 1
                    if i>=len(s):
                        break
            diagonal = not diagonal
        return ''.join(d[j] for j in range(0, numRows))
