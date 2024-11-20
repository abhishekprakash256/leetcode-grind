"""

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal 
of the same tree, construct and return the binary tree.


"""

"""

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]


"""


"""
approach -- 

  3
 / \
9  20
   /\
  15 7

preoder - root,left,right  
inorder - left,root, right 


[3,9,20,15,7] - preorder
 
[9,3,15,20,7] - inorder 

root = 3 





"""

class Solution(object):
    def buildTree(self, preorder, inorder):
    	"""
		The function to make the tree
    	"""

        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root