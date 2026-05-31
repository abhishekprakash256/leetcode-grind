"""
find the next dday that the tempr will be higher than the next day 
"""


temps = [73,74,75,71,69,72,76,73]

answer = [1,1,4,2,1,1,0,0]



class Solution():

	def dailyTemperatures(self, temps) :

		#make the stack 
		stack = []

		#results
		res = [0] * len(temps)

		for i , temp in enumerate(temps):

			while stack and temps[stack[-1]] < temp :

				index = stack.pop()

				res[index] = i - index

			stack.append(i)

		return res


sol = Solution()


res = sol.dailTemperatures(temps)


print(res)