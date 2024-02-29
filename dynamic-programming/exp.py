class Solution():

    def helper(self, nums, count):
        """
        The function to find the counter
        """

        # base cases
        if nums == 0:
            return 1  # 1 way to climb 0 steps
        if nums == 1:
            return 1  # 1 way to climb 1 step

        # Count ways for remaining steps after taking 1 step and 2 steps respectively
        return self.helper(nums - 1, count + 1) + self.helper(nums - 2, count + 1)

    def steps(self, nums):
        """
        the main function
        """

        # base case
        if nums == 0:
            return 1  # 1 way to climb 0 steps
        if nums == 1:
            return 1  # 1 way to climb 1 step

        # Initialize count to accumulate ways
        count = 0

        # Call helper function to calculate the total ways
        count = self.helper(nums, count)

        return count

# Example usage:
sol = Solution()
print(sol.steps(5))  # Output should be 3 (3 ways: {1, 1, 1}, {2, 1}, {1, 2})
