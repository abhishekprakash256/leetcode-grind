class MinStack:
	"""
	passes leetcode
	"""

	def __init__(self):
		self.stack = []       # Main stack to store all values
		self.min_stack = []   # Stack to store minimum values at each push


	def push(self, val: int) -> None:
		# Push the value onto the main stack
		self.stack.append(val)
		
		# Push onto the min stack if it's empty or the new val is the current minimum
		if not self.min_stack or val <= self.min_stack[-1]:
			self.min_stack.append(val)



	def pop(self) -> None:
		# Pop from both the main stack and min stack to keep them synchronized
		if self.stack:
			
			if self.stack[-1] == self.min_stack[-1]:

				self.stack.pop()
				self.min_stack.pop()

			else:

				self.stack.pop()



	def top(self) -> int:
		# Return the top element of the main stack
		if self.stack:
			return self.stack[-1]
		return None  # In case the stack is empty



	def getMin(self) -> int:
		# Return the top element of the min stack, which is the minimum value
		if self.min_stack:
			return self.min_stack[-1]
		return None  # In case the stack is empty