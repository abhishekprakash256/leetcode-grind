"""

"""

class Solution():

	def canJump(self,nums):
		"""
		The function to find the brute force soln of can jump 
		"""

		gas = 0 

		for n in nums:

			if gas < 0 :
				return False
		
			elif n > gas:
				gas = n 
			
			gas -=1
		
		return True