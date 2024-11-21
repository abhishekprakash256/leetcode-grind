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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # Base case
        if not inorder:
            return None
        
        # The last element of postorder list is the root
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        # Find the position of the root in the inorder list
        inorder_index = inorder.index(root_val)
        
        # Recursively build the left and right subtrees
        root.right = self.buildTree(inorder[inorder_index+1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)
        
        return root
