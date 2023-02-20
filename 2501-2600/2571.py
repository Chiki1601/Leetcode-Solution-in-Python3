class Solution:
   def minOperations(self, n: int) -> int:
        res = 0
        while n > 0:
            if n % 2 == 0:
                n >>= 1
            elif (n & 2) > 0:
                n += 1
                res += 1
            else:
                res += 1
                n >>= 2
        return res
