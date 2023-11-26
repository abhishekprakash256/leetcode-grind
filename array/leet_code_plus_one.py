"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

"""


#test case 

nums = [1,2,3]
out = [1,2,4]

nums2 = [9]
out2 = [1,0]

nums3 = [1,2,9]
out3 = [1,3,0]

nums4 = [9,9]
out4 = [1,0,0]

nums5 = [1,0,0,0]
out5 = [1,0,0,1]


#print(34%10)  #add
#print(34//10)  #carry 



class Solution(object):
	def plusOne(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""

		sum_lst = []
		carry = 1

		for i in reversed(digits):


			sum = carry + i
			add = sum % 10 
			carry = sum //10


			sum_lst.append(add)


		if carry != 0:

			sum_lst.append(carry)

		sum_lst.reverse()

		return sum_lst



if __name__ == "__main__":

	sol = Solution()

	res = sol.plusOne(nums)

	print(res)