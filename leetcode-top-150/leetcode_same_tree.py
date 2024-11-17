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
    def traverse(self, node):
        """
        The traverse function that returns the value of the node
        or None if the node is None.
        """
        return None if not node else node.val

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        The main checking function to determine if two trees are the same.
        passes leet code 
        """

        # Base case: both trees are empty
        if not p and not q:
            return True

        # If one tree is empty and the other is not
        if not p or not q:
            return False

        # Check current node values
        if self.traverse(p) != self.traverse(q):
            return False

        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)






		

		




		 

