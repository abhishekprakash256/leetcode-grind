"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

"""
algo -- 

recursion 

base :
if node.left is None and node.right is None:
	return True


def helper(node):

	return node.val



def isSymetric(self,node):
	
	#base case 
	if node.left is None and node.right is None:
		return True


	
	left_val = self.helper(node.left) if node.left else None 
	right_val = self.helper(node.right) if node.right else None 

	if left_val == right_val:
		return True 

	else :
		return False