    def minOperations(self, A: List[int], B: List[int]) -> int:
        v = B[-1]
        res = 0
        last = inf
        for a, b in zip(A, B):
            res += abs(a - b)
            if a <= v <= b or b <= v <= a:
                last = 0
            last = min(last, abs(a - v), abs(b - v))
        return res + last + 1
