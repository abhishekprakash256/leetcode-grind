"""
make the monotonic stack 
both increasing and descreasing 
"""


nums = [5,1,2,3,10]



class Solution():

    def make_increasing_stack(self, nums):
        """
        The function to create a monotonic increasing stack.
        This stack maintains elements in increasing order (bottom to top).
        """
        stack = []

        for i in range(len(nums)):
            # Maintain increasing order
            while stack and nums[i] < stack[-1]:

                stack.pop()  # Pop elements until order is restored

            stack.append(nums[i])  # Push the current element

        return stack


    def make_decreasing_stack(self, nums):
            """
            The function to create a monotonic decreasing stack.
            This stack maintains elements in decreasing order (top to bottom).
            """
            stack = []

            for i in range(len(nums)):
                # Maintain decreasing order in the stack
                while stack and nums[i] > stack[-1]:
                    stack.pop()  # Pop elements until order is restored
                stack.append(nums[i])  # Push the current element

            return stack

sol = Solution()

print("increasing stack")
print(sol.make_increasing_stack(nums))

print("decreasing stack")
print(sol.make_decreasing_stack(nums))