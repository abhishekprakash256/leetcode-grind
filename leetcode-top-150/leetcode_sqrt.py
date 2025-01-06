"""
find the sqaure root of the number 


Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

"""


"""

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 


"""

"""
prev_val = 1 

for i in raneg(1,x//2) :

	val = i*i

	if val > x :

		return prev_val

	
	prev_val = val



"""



class Solution_slow():

	def mySqrt(self, x: int) -> int:
		"""
		The function to find the sqrt
		passes leetcode
		use binary search for better approach 
		"""
		#constraint 
		if x == 0 :
			return 0

		#base case 
		prev_val = 1

		for i in range(1, (x//2) + 2 ) :

			val = i*i

			if val == x:

				return i

			elif val > x:
				return prev_val

			prev_val = i



class Solution():

	def mySqrt(self,x) -> int:
		"""
		The function to find the sqrt of the integer
		passes leetcode
		"""

		#constraints 
		if x == 0 :
			return 0 

		if x == 1 :

			return 1


		#left and right pointer
		l , r = 1 , x 

		#start the loop
		while l <= r :

			mid = (l + r) // 2 

			sqr = mid * mid 

			if sqr == x :

				return mid 


			elif sqr < x :

				l = mid + 1

			else :

				r = mid -1

		return l - 1














if __name__ == "__main__":

	sol = Solution()
	print(sol.mySqrt(6))



