class Solution:
	def pivotInteger(self, n: int) -> int:

		nth_sum = n*(n+1)//2

		pivot_elements = {0:0}

		current_sum = 0

		for num in range(1,n+1):
			current_sum = current_sum + num
			pivot_elements[num] = current_sum

		for key in range(1,n+1):

			remaining_sum = nth_sum - pivot_elements[key - 1]

			if remaining_sum == pivot_elements[key]:
				return key

		return -1
