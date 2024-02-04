"""
find the missing postive in the array 
smallest positive array 
"""


"""
find the missing postive integer

min_pos_num = 1 
it's not sorted ,so min sort time is nlogn 

one scan is O(n)

#brute force approach

mapper = {1}

if nums[i] in mapper:
	min_pos_num +=1

else:
	map[nums[i]] = True

"""

#test cases

nums = [0,-1,3,5]
out = 1


nums2 = [1,5,2]
out2 = [3]


nums3 = [1,1]
out3 = 2



#---------------------------all solutions are incorrect ----------------------------------------------

class Solution():

	def firstMissingPositive(self, nums) -> int:
		"""
		The function to find the minimum missing 
		positive integer in the array 
		"""

		#initilization 

		mapper = {}
		min_num ,count= 1, 0
		mapper[min_num] = True


		#start the loop 
		for i in nums:

			if i in mapper: 

				count +=1

				if count == 1:
					min_num +=1

			if i == min_num and count == 0:
				min_num +=1


			else:
				mapper[i] = True



		return min_num



class Solution():
	def firstMissingPositive(self, nums) -> int:
		"""
		The function to find the minimum missing 
		positive integer in the array 
		"""

		# Initialization
		mapper = {}
		min_num, count = 1, 0

		# Start the loop
		for i in nums:
			if i in mapper:
				count += 1
				if count == 1:
					min_num += 1
			elif i == min_num and count == 0:
				min_num += 1
			else:
				mapper[i] = True

		return min_num


class Solution():
	def firstMissingPositive(self, nums) -> int:
		"""
		The function to find the minimum missing 
		positive integer in the array 
		"""

		# Initialization
		mapper = {}
		min_num, count = 1, 0

		# Start the loop
		for i in nums:
			if i > 0:
				mapper[i] = True
				if i == min_num:
					count += 1
					while mapper.get(min_num):
						min_num += 1
					count = 0

		return min_num



if __name__ == "__main__":
	pass




		
