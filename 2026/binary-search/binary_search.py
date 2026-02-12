"""
Make a simple binary search
"""

class Solution():

	def binary_search(self,nums , target):
		"""
		The function to find the target using binary search
		"""

		#ptrs 
		l , r = 0 , len(nums) - 1

		#start the loop
		while l <= r :

			m = (l + r) // 2

			print(nums[m])

			if nums[m] == target :

				return True


			if nums[m] < target :

				l = m + 1

			else :

				r = m - 1


		return False 




if __name__ == "__main__":

	sol = Solution()

	target = 5 
	
	nums = [1,1,1,3,3,3,4,5,5,5,6,7]

	res = print(sol.binary_search(nums , target))

	print(res)