class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        totals = defaultdict(int)

        for a, b in itertools.combinations(nums, 2):
            totals[a * b] += 1

        return sum(4 * v * (v - 1) for v in totals.values() if v > 1)
