class Solution:
    def passThePillow(self, n, time):
        return n - abs(n - 1 - time % (n * 2 - 2))
