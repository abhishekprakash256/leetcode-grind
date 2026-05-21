"""
find the next dday that the tempr will be higher than the next day 
"""


temps = [73,74,75,71,69,72,76,73]

answer = [1,1,4,2,1,1,0,0]



class Solution():

	def dailTemperatures(self, temps) :

		#make the stack 
		stack = []

		#results
		res = [0] * len(temps)

		current = temps[0]

		for i , temp in enumerate(temps) :

			#put in the stack
			while stack and stack[-1] < current :

				current = stack.pop()

			print(stack)
			
			stack.append(temp)





sol = Solution()


res = sol.dailTemperatures(temps)


print(res)