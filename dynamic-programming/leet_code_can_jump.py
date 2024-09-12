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


class Solution3:
    def canJump(self, nums: List[int]) -> bool:
        """
        DP solution to determine if you can reach the last index
        Time limit exceeded 
        """
        n = len(nums)
        dp = [False] * n  # Create a DP array to track if each index is reachable
        dp[0] = True  # The first index is always reachable

        # Iterate through each index and check if it's reachable
        for i in range(1, n):
            for j in range(i):
                if dp[j] and j + nums[j] >= i:  # If j is reachable and we can jump to i
                    dp[i] = True
                    break  # No need to check further if we can already reach i

        return dp[-1]  # Return True if the last index is reachable, False otherwise