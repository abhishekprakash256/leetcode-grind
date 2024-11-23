"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up 
all the values along the path equals targetSum.

A leaf is a node with no children.
"""


"""


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.



Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

"""


"""
approach 

use dfs 

make the sum zero on start 

sum = 0 

carry_sum = 0 





"""




class Solution(object):
    def dfs_sum(self, node, temp_sum):
        """
        Helper function to find the sum using DFS.
        """
        if not node:  # Base case: reached a null node
            return False

        # Add the current node's value to the running sum
        temp_sum += node.val

        # Check if it's a leaf node and the path sum equals the target
        if not node.left and not node.right:
            return temp_sum == self.targetSum

        # Recur for left and right subtrees and return True if any path matches
        left = self.dfs_sum(node.left, temp_sum)
        right = self.dfs_sum(node.right, temp_sum)

        return left or right

    def hasPathSum(self, root, targetSum):
        """
        Main function to determine if a path with the given sum exists.
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        self.targetSum = targetSum

        # Base case: If the tree is empty, no path exists
        if not root:
            return False

        # Start the DFS traversal
        return self.dfs_sum(root, 0)


