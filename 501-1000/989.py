class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        s = "".join(str(num[i]) for i in range(len(num)))
        ss = str(int(s) + k)
        return [int(i) for i in ss]
