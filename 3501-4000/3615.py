class Solution:
    
    
    def recur(self,i,j,vi,dp,label,graph,connect):
        #print(i,j,bin(vi))
        if i==j:
            return 1
        ans=0
        if dp[i][j][vi]!=-1:
            return dp[i][j][vi]
        for k in graph[i]:
            if (1<<k) & vi :
                continue
            for w in graph[j]:
                if (1<<w) & vi :
                    continue
                if label[k]!=label[w]:
                    continue
                e=self.recur(k,w,vi | (1<<k) | (1<<w) ,dp,label,graph,connect)
                if e>0:
                    ans=max(ans,e)
        if ans==0 and connect[i][j]==0:
            dp[i][j][vi]=0
            return 0
        dp[i][j][vi]=ans+2
        return dp[i][j][vi]

                
        
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        dp=[[[-1 for i in range(1<<(n+1))] for j in range(n+1)] for k in range(n+1)]
        graph={i:set() for i in range(n)}
        connect=[[0 for i in range(n+1)] for j in range(n+1)]
        for i in edges:
            graph[i[0]].add(i[1])
            graph[i[1]].add(i[0])
            connect[i[0]][i[1]]=1
            connect[i[1]][i[0]]=1
    
        ans=1
        print(graph)
        for i in range(n):
            for j in range(n):
                if label[i]==label[j] :
                    ans=max(ans,self.recur(i,j,(1<<i ) | (1<<j) ,dp,label,graph,connect))
                    #print("____")
            
        return ans
        
