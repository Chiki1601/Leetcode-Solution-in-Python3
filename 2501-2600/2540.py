class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        return min(sorted(set(nums1) & set(nums2)), default=-1)
