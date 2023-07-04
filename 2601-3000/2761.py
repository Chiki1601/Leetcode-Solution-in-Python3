primes = [False,False] + [True] * 999_999               #
                                                        #
for i in range(2, 1001):                                # <-- sieve construction
    if primes[i]:                                       # 
        for j in range(i + i, 1000_000, i):             #
            primes[j] = False                           #

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:

        if n < 4: return []                             # 
                                                        # <-- edge cases
        if n%2 or n == 4:                               #
            return [[2,n-2]] if primes[n-2] else []     #

        return [[i, n - i] for i in range(3,(n+3)//2)   # <-- find pairs
                       if primes[i] and primes[n - i]]  #
