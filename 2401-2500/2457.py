class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digit_sum(n):
            return sum([int(c) for c in str(n)])
        
        lst = 1 
        add = 0
         
        while digit_sum(n + add) > target:
            x = 10 ** lst
            add = x - n % x
            lst += 1
        
        return add
