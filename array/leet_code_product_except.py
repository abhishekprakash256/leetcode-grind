"""
The Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

"""

#test

arr = [1,2,3,6]
out = [36,18,12,6]


arr2 = [1,0,0,2]
out2 = [0,0,0,0]

arr3 = [-1,3,2]
out3 = [6,-2,-3]


class Solution(object):
	def productExceptSelf1(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""

		prefix = []
		postfix = []
		pre_mul, post_mul = 1,1 


		for i in nums:
			
			pre_mul = pre_mul * i
			prefix.append(pre_mul)

		for i in nums[::-1]:

			post_mul = post_mul * i
			postfix.insert(0,post_mul)


		mul_arr = []
		mul_arr.append(prefix[0])


		l,r = 0,2

		while r < len(nums):

			val = prefix[l]*postfix[r]
			mul_arr.append(val)
			l +=1
			r +=1

		mul_arr.append(prefix[l])

		return mul_arr


if __name__ == "__main__":

	sol = Solution()

	res = sol.productExceptSelf1(arr)

	print(res)
		
