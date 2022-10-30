class Solution:
    def oddString(self, words: List[str]) -> str:
        
        # [1] as stated in the problem, there will be two groups 
        #     of words according to their difference array;
        #     we'll store them in a hashmap/dict using the
        #     difference array as a key
        eq = defaultdict(list)
        
        for w in words:
            # [2] in Python, keys are immutable, thus we convert
            #     the difference array to 'tuple'
            diff = [ord(a)-ord(b) for a, b in zip(w[:-1], w[1:])]
            eq[tuple(diff)].append(w)
        
        # [3] as guaranteed in the problem, there will be 2
        #     groups of words, one of them of size 1
        for _, ws in eq.items():
            if len(ws) == 1:
                return ws[0]
