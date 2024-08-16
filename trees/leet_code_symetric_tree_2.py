"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Constraints:

	1 <= nums.length <= 104
	-104 <= nums[i] <= 104
	nums is sorted in a strictly increasing order.

"""


"""
approach 

1. using recursion

def node_val(node):

	if not node:
		return 0 

	else:
		return node.val 



def helper(node_l,node_r):

	if self.node_val(node_l) == self.node_val(node_r): 
		return True

	else:
		return False

	return self.helper(node_l.left,node_r.right) and self.helper(node_l.right, node_r.left)


def isSymetric(node):

	if not node:
		return True

	if node.left is None and node.right is None:
		return True

	return self.helper(node.left, node.right)



"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

	def node_val(self,node):

		if not node:
			return 0 

		else:
			return node.val


	def helper(self, node_l: Optional[TreeNode], node_r: Optional[TreeNode]) -> bool:
		# Both nodes are None: trees are symmetric
		if not node_l and not node_r:
			return True
		
		# One of the nodes is None: trees are not symmetric
		if not node_l or not node_r:
			return False
		
		# Both nodes are not None, compare values
		if node_l.val != node_r.val:
			return False

		# Recursively check mirrored subtrees
		return self.helper(node_l.left, node_r.right) and self.helper(node_l.right, node_r.left)




	def isSymmetric(self, node: Optional[TreeNode]) -> bool:

		#edge case
		if not node:
			return True

		if node.left is None and node.right is None:
			return True


		return self.helper(node.left,node.right)

        















