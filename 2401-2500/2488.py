class Solution:
        def countSubarrays(self, nums: List[int], k: int) -> int:
            prefix_sum_of_balance = Counter([0]) # Dummy value of 0's frequency is 1.
            running_balance = ans = 0
            found = False
            for num in nums:
                if num < k:
                    running_balance -= 1
                elif num > k:
                    running_balance += 1
                else:
                    found = True
                if found:
                    ans += prefix_sum_of_balance[running_balance] + prefix_sum_of_balance[running_balance - 1]    
                else:
                    prefix_sum_of_balance[running_balance] += 1
            return ans
