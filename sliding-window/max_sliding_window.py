"""
find the max sliding windown in the array 
"""


"""
Algo -- 

l = 0 
r = 0 

 



"""







class Solution():



	def find_max_sliding_window_bruteforce(nums, w):

		# Replace this placeholder return statement with your code
		res = []
		for i in range(len(nums)-w + 1):
			cur_max = max(nums[i:i+w])
			res.append(cur_max)

		return res


	def max_sliding_window(self,nums,w):
		"""
		The function to find the max sliding window 
		"""
		pass





