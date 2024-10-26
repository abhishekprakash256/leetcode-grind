"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

"""

"""
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


"""



"""

res_lst = []
nums.sort()

for i in range(len(nums)):
	
	#pointers
	j = i + 1
	k = len(nums) - 1

	while j < k:

		#sum
		sum = nums[i] + nums[j] + nums[k]

		if sum == 0 and nums[i] != nums[j] and nums[i] != nums[k]and nums[j] != nums[k] and [[nums[i],nums[j],nums[k]] not in res_lst:

			res_lst.append([[nums[i],nums[j],nums[k]])

		elif sum > 0:

			k -= 1

		else:

			j += 1


"""


from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        The function to find the unique triplets in the array that sum up to zero.
        passes leetcode
        """
        res_lst = []
        nums.sort()

        for i in range(len(nums) - 2):
            # Skip duplicate values for `i` to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two-pointer approach
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum == 0:
                    res_lst.append([nums[i], nums[j], nums[k]])
                    
                    # Skip duplicates for `j` and `k` after a successful triplet is found
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    
                    # Move pointers after handling duplicates
                    j += 1
                    k -= 1

                elif sum < 0:
                    j += 1
                else:
                    k -= 1

        return res_lst













