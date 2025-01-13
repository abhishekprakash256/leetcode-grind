"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

"""

"""
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

 
Constraints:

1 <= numRows <= 30


"""

"""
approach -- 




"""




class Solution():

	def generate(self, numsRows) :
		"""
		The function to make the pascal traingle
		"""

		#constarints
		if numsRows == 1 :

			return [[1]]

		if numsRows == 2 :

			return [[1],[1,1]]

		#result list
		res_lst = [[1],[1,1]]

		for i in range(1,numsRows-1) :

			temp_lst = [1]

			for j in range(i) :

				temp_lst.append(res_lst[i][j] + res_lst[i][j+1])

			temp_lst.append(1)

			res_lst.append(temp_lst)


		return res_lst




sol = Solution()

print(sol.generate(5))