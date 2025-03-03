"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

"""


"""

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""


"""
approach -- 

traversal 

dfs or bfs 

running sum 

max_sum = -inf 

curr_sum = node.val + max(lef,right)



"""





class Solution:
    """
    passes leetcode
    """

    def __init__(self):

        self.result = float("-inf")

    def helper_dfs(self,node):
        """
        The function to find the max path sum
        """

        #base case 

        if not node :

            return 0 

        #dfs calls with ignoring the negative values 
        left = max(0 , self.helper_dfs(node.left) ) 
        right = max(0, self.helper_dfs(node.right) ) 

        self.result = max(self.result , node.val + left + right)

        return node.val + max(left, right)


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        The function to find the max path sum 
        """

        #constraint case 
        if not root.left and not root.right :

            return root.val

        #helper dfs call
        self.helper_dfs(root)

        return self.result

