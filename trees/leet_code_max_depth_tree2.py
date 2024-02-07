"""
make a program to find the max depth of the tree
height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""


"""
Algo - 

recursive approach --- 

input head - 
height 

#base case of exit 

if node is none:
	return 0 

if node.left is none and node.right is None:
	retun 1


#left node is there 

	recursive call on left part with height + 1


#right node is there 
	recursive call of right part with height + 1


return height


#helper(self,node,height = 0 )


#main function 
def maxDepth(self,node):


"""
#all soln works
class Solution:
    def helper(self, node, height=0):
        # Base case: if the node is None, return the current height
        if node is None:
            return height
        
        # Recursive calls to get the height of the left and right subtrees
        left_height = self.helper(node.left, height + 1)
        right_height = self.helper(node.right, height + 1)
        
        # Return the maximum height among the left and right subtrees
        return max(left_height, right_height)
    
    def maxDepth(self, node):
        # Call the helper function with the root node
        return self.helper(node)
    


class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left) + 1
        right_depth = self.maxDepth(root.right) + 1

        return max(left_depth, right_depth)

