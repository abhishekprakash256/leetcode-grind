"""
Make a simple binary search
"""

class Solution():

	def binary_search(self,nums , target):
		"""
		The function to find the target using binary search
		"""

		#ptrs 
		l , r = 0 . len(nums) - 1

		#start the loop
		while l <= r :

			m = (l + r) // 2

			if nums[m] == target :

				return True


			if nums[m] < target :

				r = m - 1

			else :

				l = m + 1


		return False 



