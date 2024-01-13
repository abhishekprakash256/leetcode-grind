"""
make a progrma to give the sum of the elements to the non negative number 
"""


class Solution():

	def make_sum_iter(self,n):

		sum = 0 

		for i in range(n+1):

			sum +=i

		return sum



	def make_sum_rec(self,n):

		if n == 0:

			return 0
		else:

			return n + self.make_sum_iter(n-1)





if __name__ == "__main__":

	sol = Solution()

	res = sol.make_sum_iter(3)
	res2 = sol.make_sum_rec(3)


	print(res)
	print(res2)