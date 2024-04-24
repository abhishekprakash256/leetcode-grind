"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Input: n = 19
Output: true



1 + 81 = 82 
64 + 4 = 68 
36 + 64 = 100 
1 + 0 + 0 = 1




"""


"""

use a hasmap to find the replication of value 

#base case 
if nums == 1:
	return True 


#hash map 
mapper = {}

#sum = 0 

#start the loop


while True:	

	if sum == 1:
		return True
		break

	elif sum in mapper:
		return False
		break

	while num:

		sum = 0
		
		val = nums % 10 

		sum += val*val

		num = num // 10
	
	num = sum

	mapper[num] = True













"""


nums = 19 

class Solution():

	def isHappy(self,nums):
		"""
		The function to check if the number is happy or not 
		"""

		#base case 
		if nums == 1:
			return True


		#vars 
		mapper = {}
		

		#start the loop 

		while True:

			if nums == 1:
				return True
				break

			elif nums in mapper:
				print(nums)
				return False
				break

			mapper[nums] = True

			sum_num = 0

			while nums:

				val = nums % 10 

				sum_num += val*val

				nums = nums // 10 

			nums = sum_num

			





if __name__ == "__main__":

	sol = Solution()
	print(sol.isHappy(nums))