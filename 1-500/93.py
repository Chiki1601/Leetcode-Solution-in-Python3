class Solution:
    def backtrack(self,original,dots,ans,idx,cur):
        if dots==4:
            tmp=cur[:len(cur)-1]
            if len(tmp)-3==len(original):
                ans.append(tmp)
            return
        tmp=''
        for i in range(idx,len(original)):
            tmp+=original[i]
            if 0<=int(tmp)<=255 and not(tmp[0]=='0' and len(tmp)>1):
                self.backtrack(original,dots+1,ans,i+1,cur+tmp+'.')
            else:break
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans=[]
        self.backtrack(s,0,ans,0,'')
        return ans
