"""

"""

class Solution():

	def canJump(self,nums):
		"""
		The function to find the brute force soln of can jump 
        The code works in leetcode
		"""

		gas = 0 

		for n in nums:

			if gas < 0 :
				return False
		
			elif gas < n:
				gas = n 
			
			gas -=1
		
		return True
	

class Solution2():
    def canJump(self, nums: List[int]) -> bool:
        """
        The function to find the jump possible
        The code works in leetcode
        
        """
        
        gas = 0 
        
        for i in nums:
            
            if gas < 0:
                return False
            
            elif gas < i:
                gas = i
            
            gas -= 1
        
        return True
        