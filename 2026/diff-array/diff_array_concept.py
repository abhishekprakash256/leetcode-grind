"""
The file for the diff aray concept
"""



class Solution():

	def range_addition(self, n , updates):
		"""
		The function to make the array of from the range
		"""

		#make the diff array
		diff = [0] * n

		#make the limits 
		for l ,r , val in updates :

			diff[l] += val

			if r + 1 < n :

				diff[r+1] -= val

		#make the arr
		res = [0] * n
		res[0] = diff[0]


		#put the value in array
		for i in range(1,n):

			res[i] = res[i - 1] + diff[i]


		return res



if __name__ == "__main__" :

	sol = Solution()

	updates = [(1, 3, 2), (2, 4, 3)]

	res = sol.range_addition(5 , updates)

	print(res)

