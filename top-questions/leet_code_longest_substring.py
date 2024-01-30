"""
make the longest substring from the given string without repeating character
"""

#test cases 
string = "abcbfd"
out = 4

string2 = "cccc"
out2 = 1

string3 = "cabdf"
out3 = 5

string4 = "fffhja"
out4 = 4



class Solution():

	def longestString(self,string):
		"""
		The function to find the longest string without repearing character
		"""

		#initilaize the set
		str_set = set()

		#initilaize the pointers
		l = 0
		res = 0

		for i in range(len(string)):

			while string[i] in str_set:

				str_set.remove(string[l])

				l +=1

			str_set.add(string[i])

			res = max(res, i - l + 1)


		return res



if __name__ == "__main__":

	sol = Solution()

	res = sol.longestString(string2)

	print(res)
