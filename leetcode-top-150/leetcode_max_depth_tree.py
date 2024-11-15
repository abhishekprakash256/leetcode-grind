"""
Find the max depth of the binary tree 
"""


"""

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
"""


"""
approach using recursion 


if node:
    
    if node.left :
        self.height(node.left,height + 1)
    
    if node.right : 
        self.height(node.right, height + 1)

return height 




"""


class Solution:

    def height_tree(self,node,height):
        """
        The helper funciton 
        """

        #base case 
        if not node:
            return height
        

        left = self.height_tree(node.left, height + 1)

        right = self.height_tree(node.right, height +1 )
        
        return max(left,right)


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        The function to get the max depth of the Binary Tree
        passes leet code
        """

        #base case 
        if not root :
            return 0


        #make the height 
        height = 0

        return self.height_tree(root,height)
