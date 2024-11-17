"""
the function to find the tree are same 

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value.
"""


"""
Input: p = [1,2,3], q = [1,2,3]
Output: true


"""


"""
approach 

traversal problem 

def traverse(self,node):

	if not node:
		return None
	
	self.traverse(node.left)
	self.traverse(node.right)

	return node.val


		
def main(self,node):   

	#base case 
	if not node :
	 
		return None

	left = self.traverse(node.left)
	right = self.traverse(node.right)

	if left == right :
		return True
	
	else:
		
		return False


"""

class Solution:

	def traverse(self,node):
		"""
		The traverse function 
		"""

		if not node :
			return None
	

		return node.val

	def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
		"""
		The main checking function
		"""


		#base case 

		if not p and not q : 

			return True


		if not p and q : 

			return False

		if p and not q :

			return False


		if p and q :

			if self.traverse(p.left) != self.traverse(q.left) : 

				return False


			if self.traverse(p.right) != self.traverse(q.right) : 

				return False


		return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) 







		

		




		 

