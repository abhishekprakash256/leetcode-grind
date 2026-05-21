""""
The template for monotonic stack
"""


nums = [73,74,75,71,69,72,76,73]

#answer = [1,1,4,2,1,1,0,0]



stack = []

for i in range(len(nums)):

	while stack and stack[-1] < nums[i]:

		prev = stack.pop()

		# nums[i] is next greater for prev

	stack.append(nums[i])



print(stack)
