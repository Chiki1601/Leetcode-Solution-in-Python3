class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        heap = []                               # Example: gifts = [25,64,9,4,100] ; k = 4

        for g in gifts: heappush(heap,-g)       # heap = [-100,-64,-25, -9,-4]
                     
                                                #    g    isqrt(g)        heap
        g = -heappop(heap)                      #  –––––  ––––––––  –––––––––––––––––
                                                #   100     10      [-64,-25, -9, -4]
        for _ in range(k):                      #    64      8      [-25,-10, -9, -4]      
            g = -heappushpop(heap, -isqrt(g))   #    10      3      [-10,- 8, -9, -4]
                                                #     9             [- 8, -4, -5, -3]
        
        return g - sum(heap)                    # return 9 - sum(- 8, -4,-5,-3) = 29
