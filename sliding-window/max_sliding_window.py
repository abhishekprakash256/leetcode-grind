"""
find the max sliding windown in the array 
"""


class Solution():



	def find_max_sliding_window_bruteforce(nums, w):

		# Replace this placeholder return statement with your code
		res = []
		for i in range(len(nums)-w + 1):
			cur_max = max(nums[i:i+w])
			res.append(cur_max)

		return res


	def find_max_sliding_window(nums,w):
		"""
		The function to find the max in the sliding window
		"""

		res = []
		count = 0 
		max_val = nums[0]

		for i in range(len(nums)):
				
			count += 1
			
			if count == w :
				res.append(max_val)
				count = 0 
				max_val = nums[i+1]


			cur_max = nums[i]
			max_val = max(cur_max,max_val)


		return res



