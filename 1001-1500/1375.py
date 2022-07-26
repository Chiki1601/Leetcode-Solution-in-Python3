from typing import List

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        n = len(light)
        flag = [False] * (n+1)
        cnt_blue, cnt_light = 0, 0
        max_i = 0
        for i in range(n):
            flag[light[i]] = True  
            cnt_light += 1
            max_i = max(max_i, light[i])
           
            if cnt_light == max_i:
                cnt_blue += 1
        return cnt_blue

if __name__ == "__main__":
    light = [1,2,3,4,5,6]
    print(Solution().numTimesAllBlue(light))  
