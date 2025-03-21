"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined 
between two nodes p and q as the lowest node in T that has both p and q as
 descendants (where we allow a node to be a descendant of itself).”
"""

"""


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.

"""


"""
approch -- 

using dfs we get levels ? 

we find both and trace path ? 

stack structure ?? 

append the nodes and pop as we found both ? 




"""


class Solution():
    """
    passes leetcode
    """

    def _helper_dfs(self,node, p , q) :
        """
        The function to do the dfs for the node traversal 
        """

        #base case 

        if not node or node == p or node == q:

            return node

        #left and right calls 
        left = self._helper_dfs(node.left , p , q )

        right = self._helper_dfs(node.right , p , q )


        if left and right:

            return node


        if left:
            return left

        else :
            return right
        


    def lowestCommonAncestor(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        """
        The function to find the lowest common ancestor
        """     

        #call the helper function 
        return self._helper_dfs(root, p , q )

