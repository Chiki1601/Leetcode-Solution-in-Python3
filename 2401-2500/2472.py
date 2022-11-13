class Solution:
    def maxPalindromes(self, S: str, k: int) -> int:
        N, intervals, last, ans = len(S), [], -inf, 0
        for center in range(2 * N - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < N and S[left] == S[right]:
                if right + 1 - left >= k: 
                    intervals.append((left, right + 1))
                    break
                left -= 1
                right += 1
        for x, y in intervals:
            if x >= last:
                last = y
                ans += 1
            else:
                if y < last: last = y
        return ans
