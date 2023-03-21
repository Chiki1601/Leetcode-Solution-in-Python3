class Solution:
    def repairCars(self, A: List[int], cars: int) -> int:
        return bisect_left(range(10**14), cars, key=lambda x: sum(int(sqrt(x / a)) for a in A))
