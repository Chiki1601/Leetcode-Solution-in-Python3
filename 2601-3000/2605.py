class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = set(nums1), set(nums2)
        if s1 & s2:
            return sorted(s1 & s2)[0]
        nums1.sort()
        nums2.sort()
        a, b = nums1[0], nums2[0]
        return min(a, b) * 10 + max(a, b)
