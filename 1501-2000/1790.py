class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        return len(D:=[(x, y) for x, y in zip(s1, s2) if x!=y])==0 or (len(D)==2 and D[0][0]==D[1][1] and D[0][1]==D[1][0])               
