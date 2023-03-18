class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        c=0
        for i in range(left,right+1):
            if(words[i][0]=='a' or words[i][0]=='e' or words[i][0]=='i'or words[i][0]=='o' or words[i][0]=='u')and ( words[i][-1]=='a' or words[i][-1]=='e' or words[i][-1]=='i'or words[i][-1]=='o' or words[i][-1]=='u'):
                c+=1
        return c
