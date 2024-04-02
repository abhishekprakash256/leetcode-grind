"""
the perfect squares to find in the given number 
"""

class Solution():

	def numSquares(self,n):
		"""
		The funciton to find the perfect sqaures
		"""

		dp = [n] * (n+1)
		dp[0] = 0

		for target in range(1,n+1):

			for s in range(1,target + 1):

				square = s*s

				if target - square < 0:
					break

				dp[target] = min(dp[target],1 + dp[target -square])

		return dp[n]

class Solution2():
    
    
    def dp(self, n, memo={0: 0}):
        
        if n < 0:
            return 0
        
        if n in memo:
            return memo[n]
        
        ans = n
        root = 1
        
        while root ** 2 <= n:
            ans = min(1 + self.dp(n - root ** 2), ans)
            root += 1
        
        memo[n] = ans
        
        return ans
    
    
    def numSquares(self, n: int) -> int:
        return self.dp(n)
