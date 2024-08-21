"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, 
construct and return the binary tree.
"""

"""
preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
"""

"""
preorder = [-1], inorder = [-1]
Output: [-1]
"""


"""
approach - 

1. preorder, inorder 
2. [3,9,20,15,7] , [9,3,15,20,7]
3. root_val = preorder[0]
4. mid = inorder.index(root_val)
5. root = Treenode(root_val)
6. root.left = 




"""


class Solution:
	def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
		"""
		The function to make the tree recursively using the inorder and preorder lists
		"""

		#base case 


		root = TreeNode(preorder[0])
		mid = inorder.index(preorder[0])

		#make the tree recursively

		root.left = buildTree(preorder[mid],inorder[m+1,len(inorder) - 1])
		root.right = buildTree(preorder[])



