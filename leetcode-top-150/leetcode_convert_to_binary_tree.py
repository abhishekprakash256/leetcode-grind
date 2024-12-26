"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced
binary search tree.

A max diffrence of one height
"""

"""
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""

"""

approach -- 

sorted helps 

find the middle and make the head or root node 

len(nums) // 2 = mid 

root = TreeNode(nums[mid])

root.left = self.helper()



"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

	def helper(self,i,j):
		"""
		The helper function for recusive node making
		"""

		#base case 
		if i == j :
			return 

		#make the node 
		mid = (i+j) // 2 
		node = TreeNode(self.nums[mid])

		#get the head node 
		if i == 0 and j == len(self.nums) - 1 :
			self.headnode = node

		#make the recursive node calls 
		node.left = self.helper(i,mid)
		node.right = self.helper(mid+1,j)



	def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
		"""
		The function to make the tree
		"""
		self.nums = nums

		#constraints 
		if len(nums) == 1 :
			node = TreeNode(nums[0])
			return node

		#make the recursion call
		self.helper(0,len(self.nums)-1)

		return self.headnode





