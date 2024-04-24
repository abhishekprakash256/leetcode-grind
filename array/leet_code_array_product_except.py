"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums 
except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""


"""
nums = [1,2,3,4]
out = [24,12,8,6]


algo -- 



[1,2,3,4]

[24,24,12,4] prefix

[1,2,6,24] postfix 


[24,12,8,6]




"""


nums = [1,2,3,4]

class Solution():

    def product_except_self(self,nums):
        n = len(nums)
        prefix_products = [1] * n
        suffix_products = [1] * n
        result = [0] * n

        # Calculate prefix products
        for i in range(1, n):
            prefix_products[i] = prefix_products[i - 1] * nums[i - 1]
        
        print(prefix_products)

        # Calculate suffix products
        for i in range(n - 2, -1, -1):
            suffix_products[i] = suffix_products[i + 1] * nums[i + 1]

        print(suffix_products)

        # Calculate the product of all elements except nums[i]
        for i in range(n):
            result[i] = prefix_products[i] * suffix_products[i]

        return result
    


if __name__ == "__main__":

    sol = Solution()
    print(sol.product_except_self(nums))