"""

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""


"""

Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false

"""




"""
apprach -- 

base case 

if not node : 
	return True 



if root : 

	if root.left.val , root.right.val == root.right.val , root.left.val : 
		
		True

	else:

		False

return self.isSymetric(self.left) and self.isSymetric(self.right)

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

	def isMirror(self,left,right):
		"""
		The function to find the mirror image 

		"""
		if not left and not right : 

			return True

		if not left or not right :

			return False

		return (right.val == left.val) and self.isMirror(left.left,right.right) and self.isMirror(left.right,right.left)



	def isSymmetric(self, root):
		"""
		:type root: Optional[TreeNode]
		:rtype: bool
		passes leetcode
		"""

		#base case 
		if not root : 

			return True


		#not root
		
		return self.isMirror(root.left, root.right)


		