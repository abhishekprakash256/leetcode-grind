"""
the program to climb the stairs of the given numbers 

find the number of distint way I can climb up the starirs 

either step 1 or step 2 is allowed 
"""


"""
example - 

1  - one way 
2 - 1+1 , 2 , 2 way
3 - 1,2 , 2,1, 1,1,1 - 3 ways 


decsion tree 

brute force -- 

recurive approach 

two function 



#base case -- 
if nums == 0 : 
	return 0 

if nums ==1 :
	return 1 

count = 0 

self.helper(n,count)

return count


helper(n,count)

if nums == 0 : 
	return 0 

if nums == 1 :
	return 1 


count = self.helper(nums-1,count + 1) + self.helper(nums - 2 , count + 1 )

return count

"""

import time


class Solution():

	def __init__(self):
		"""
		The caching
		"""
		self.memo = {}

	def helper(self,nums,count):
		"""
		The function to find the counter
		"""

		#base cases
		if nums == 0 :
			return 1 

		if nums == 1 :
			return 1


		count = self.helper(nums - 1,count + 1) + self.helper(nums - 2,count + 1)

		return count

	def climStairs_brute_force(self,nums):
		"""
		the main function
		"""

		#base case 
		if nums == 0 : 
			return 1 

		if nums == 1:
			return 1 


		count = 0 

		count = self.helper(nums,count)

		return count


	def helper_memo(self,nums,count):
		"""
		The helper funciion to find the climbs
		"""

		#base case 

		if nums <=1:
			return 1 

		if nums in self.memo:
			return self.memo[nums]

		self.memo[nums] = self.helper_memo(nums - 1,count + 1) + self.helper(nums - 2, count + 1)


		return self.memo[nums]



	def climStairs_memo(self,nums):
		"""
		The memoization approach
		"""
		
		#base case
		if nums <= 1 :
			return 1 


		count = 0 

		count = self.helper(nums,count)

		return count


	def climbStairs_dp(self,nums):
		"""
		the dynamic solutin of the stairs

		"""

		#base case 
		if nums <=1:
			return 1 

		#make the array 
		dp = [0]* (nums + 1)

		dp[0], dp[1] = 1,1

		for i in range(2,nums+1):

			dp[i] = dp[i -2 ] + dp[i - 1]


		return dp[nums]









sol = Solution()

# Record start time
start_time = time.time()


res = sol.climbStairs_dp(40)


end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time

print("Elapsed time:", elapsed_time, "seconds")
print(res)
