class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort(reverse=True)
        lignes = []
        for num in nums:
            for ligne in lignes:
                if num not in ligne:
                    ligne.append(num)
                    break
            else:
                lignes.append([num])
        return lignes
