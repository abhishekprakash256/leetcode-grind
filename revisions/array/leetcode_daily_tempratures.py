"""
Given an array of integers temperatures represents the daily temperatures, return an array answer 
such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

"""

"""
Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

[73,72,74,78,76]

[73,79,74,72,78,77]

[1,0,2,1,0,0]

maintain a max value 
min value as well 

maintain the max and min and compare with both and update as well 

if less than min 

add the value 

also maintain the max and min with idx values like dict and subtract the index and append it 

"""

class Solution():
	"""
	passes leetcode
	"""

	def dailyTemperatures(self, temperatures) :
		"""
		The function to find the days needed afer the tempr is high 
		"""

		length = len(temperatures)

		#constarints case 
		if length == 1 :

			return [0]

		#make the result 
		result = [0] * length

		#make the stack 
		stack = []

		for i in range(length) :

			while stack and temperatures[i] > temperatures[stack[-1]] :

				prev_val = stack.pop()

				result[prev_val] = i - prev_val

			stack.append(i)

		return result













