"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence 
as an edge connecting them. A node can only appear in the sequence at most once. 
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""

"""
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000

"""

"""
approach -- 

how to find path ? 




"""

class Solution:
    """
    passses leetcode
    """

    def __init__(self):

        self.max_sum = float("-inf")


    def helper_dfs(self,node):
        """
        The function to find the max path sum
        """

        #base case 
        if not node :

            return 0 

        left = max(self.helper_dfs(node.left),0)
        right = max(self.helper_dfs(node.right ),0) 

        temp_sum = node.val + left + right 

        self.max_sum = max(temp_sum , self.max_sum)

        return node.val + max(left, right)


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        The function to find the max path sum
        """

        if not root.left and not root.right :

            return root.val

        #traverse the tree 
        self.helper_dfs(root)

        return self.max_sum
