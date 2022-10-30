class Solution:
      def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for q in queries:
            if any(sum(c != d for c, d in zip(w, q)) <= 2 for w in dictionary):
                ans.append(q)
        return ans  
