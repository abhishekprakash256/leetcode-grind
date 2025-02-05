class Solution():

	def __init__(self) :

		self.result = []


	def make_combinations(self,temp_lst) :


		if len(temp_lst) == 2:

			self.result.append(temp_lst)

			return

		for i in range(self.n) :

			if i not in temp_lst :

				self.make_combinations(temp_lst + [i])


	def main(self,n):

		self.n = n 

		temp_lst = []

		self.make_combinations(temp_lst)

		return self.result

sol = Solution()

print(sol.main(3))

