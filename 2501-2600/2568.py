class Solution:
    def minImpossibleOR(self, A):
        A = set(A)
        return next(1 << i for i in range(32) if (1 << i) not in A)
