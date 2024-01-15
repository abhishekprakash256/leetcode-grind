"""
find the valid binary tree 
the condition is left subtree is less than the node 
and the right is greater than node 
that is a valid sutree
"""



"""
approach - 

recursive approach 

base case 

two functoion design 

one for returning value 

helper function

return node.val


bst

if not node:
	return True 


left = helper(left_tree)
right = helper(right_tree)

if left <= node.val <= right:
	return True
else:
	return False



"""


class Solution():

	def helper(self,node):

		"""
		the function to get the node val
		"""

		return node.val



	def isValidBST(self,node):
		"""
		The funciton to find the tree is valid 
		"""

		#base case 
		if not node:
			return True 

		#make the left and right tree
		left_val = self.helper(node.left)
		right_val = self.helper(node.right)

		#check the tree

		if left_val <= node.val <= right_val:

			return True

		else:

			return False




