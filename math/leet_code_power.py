"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Input: x = 2.00000, n = 10
Output: 1024.00000
"""


"""
algo 

1/2 

4 = 2^2

find a sqaure root of number 

start with 2 



for i in range(2,n//2):
		
	if i*i == target:
		return i 



"""

#the solution is slow using the brute force approach 


class Solution():

	def myPow_brute_force(self,x,n):
		"""
		The function to find the power of the number
		"""

		#base case 
		if n == 0:
			return 1 

		elif n > 0 :

			val = 1

			for i in range(n):
				val = val*x

		else:

			val = 1 
			n = 0 - n

			for i in range(n):
				val = val*x
		
			print(val)
			val = 1/val

		return val


	#recursion is slow 
	def myPow_rec(self,x,n):
		"""
		The funciton to find the power 
		"""

		#base case 
		res = 1 
		if n == 0:
			return 1
		
		if n > 0 :
			
			res = self.myPow(x,n-1)*x

		else:
			res = 1/self.myPow(x,-n)

		return res


		




	



	
	def sqrt_fun(self,nums):
		"""
		The funciton to find the square root of the number
		"""

		
		for i in range(2,nums//2):
				
			if i*i == nums:
				return i 

		return "fractional root"






if __name__ =="__main__":
	sol = Solution()

	print(sol.myPow(2,-2))

	#print(sol.sqrt_fun(20))
