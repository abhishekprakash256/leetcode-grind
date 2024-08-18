"""

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:



Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.



1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.


"""

"""
apprach 

1. using the recursion 

make the middle node all the time and connect the left and right recursively 

with the helper function 


details - 






"""

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution():


	def helper(self,nums,l,r):
		"""
		The helper function to make the tree
		"""

		while l > r:
			return None

		#calc the middle
		m = (l + r) // 2

		#make the new node
		node = TreeNode(nums[m])

		node.left = self.helper(nums,l,m-1)
		node.right = self.helper(nums,m+1,r)

		return node





	def sortedArrayToBST(self,nums):
		"""
		passes the leet code
		The function to  convert to tree
		"""

		#base case 
		if len(nums) == 1:
			return TreeNode(nums[0])


		#vars initilaization
		l , r = 0 , len(nums) - 1

		#recuriosn inilization
		return self.helper(nums,l,r)




if __name__ == "__main__":


	nums = [-10,-3,0,5,9]

	sol = Solution()
	print(sol.sortedArrayToBST(nums))