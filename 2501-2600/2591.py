class Solution:
    def distMoney(self, money: int, children: int) -> int: 
        if money < children: return -1 
        ans = 0 
        for j in range(1,children+1):
            leftmoney = money - 8       # if current child gets 8$
            leftchildren = children - j
            if leftmoney >= leftchildren: 
                money = leftmoney 
                ans += 1 
            else: 
                leftchildren = children - j + 1   # 1 is added because current child 
                                                  #  has not gotten any dollar yet
                if leftchildren == 1 and money == 4:
                    ans -= 1
                money = 0
                break
        if money > 0:       # if some money is left to distribute
            ans -= 1
        return ans
       
