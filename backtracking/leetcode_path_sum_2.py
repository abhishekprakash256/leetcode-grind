"""
Given the root of a binary tree and an integer targetSum, 
return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node.
 A leaf is a node with no children.
"""

"""
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22



Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:

Input: root = [1,2], targetSum = 0
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000


"""


"""
approach -- 

using a dfs approrach 

to find the sum 

make a list and append the values and keep adding as traversal happend 

if sum greater then discard 

if sum is equal:

    results the temp list


traversal 

user dfs approach

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



from typing import Optional , List


# TreeNode class definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Level 4
node7 = TreeNode(7)
node2 = TreeNode(2)
node5_leaf = TreeNode(5)
node1 = TreeNode(1)

# Level 3
node11 = TreeNode(11, left=node7, right=node2)
node13 = TreeNode(13)
node4_right = TreeNode(4, left=node5_leaf, right=node1)

# Level 2
node4_left = TreeNode(4, left=node11)
node8 = TreeNode(8, left=node13, right=node4_right)

# Root
root = TreeNode(5, left=node4_left, right=node8)




class Solution():

    def __init__(self):

        self.results = []

    def _helper_dfs(self,node,node_lst,curr_sum):
        """
        The function to recursive node list
        """

        #base case 
        if curr_sum > self.targetSum :

            return

        if curr_sum == self.targetSum :

            self.results.append(node_lst)

            return

        #make the traversal calls
        if not node:
            
            return

        if node.left :

            curr_sum += node.val

            self._helper_dfs(node.left, node_lst + [node.val] , curr_sum)

        if node.right :

            curr_sum += node.val

            self._helper_dfs(node.right, node_lst + [node.val] , curr_sum)



    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        The function to find the sum of the tree that are eqaul
        """

        self.targetSum = targetSum

        #constraint case 
        if not root :

            return []

        if not root.left and not root.right :

            if self.targetSum == root.val :

                return[root.val]

        #make the helper functin calls

        self._helper_dfs(root,[],0)

        return self.results


"""
           5
         /   \
        4     8
       /     / \
     11     13  4
    /  \        / \
   7    2      5   1

"""


class Tree_Helper():

    def __init__(self):

        self.results = []


    def dfs_tree_traversal(self,node) :
        """
        The function to travsers the tree in dfs
        """

        #base case 
        if not node :

            return

        self.results.append(node.val)

        if node.left :

            self.dfs_tree_traversal(node.left)

        if node.right :

            self.dfs_tree_traversal(node.right)

        return self.results





tree_helper = Tree_Helper()

res = tree_helper.dfs_tree_traversal(root)


print(res)

















