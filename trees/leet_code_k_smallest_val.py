"""
Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""

"""

Input: root = [3,1,4,null,2], k = 1
Output: 1


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

"""



"""
approach -- 

do the dfs traversal of the tree 
do a liner scan and return the kth smallest value
stack is used for dfs

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        """
        The function to find the kth smallest values in the tree
        The function passes leetcode
        """

        #base case 
        if not root:
            return None
        

        #vars 
        stack = [root]
        node_lst = []
        

        while stack:

            curr_node = stack.pop()

            if curr_node.right:

                stack.append(curr_node.right)
            
            if curr_node.left:
                stack.append(curr_node.left)
            
            node_lst.append(curr_node.val)
        
        #find the smmallest elemnt

        node_lst.sort()

        return node_lst[k-1]


    