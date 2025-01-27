"""

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence 
has an edge connecting them. A node can only appear in the sequence at most once. Note that the
path does not need to pass through the root.

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


"""


"""
approach -- 

divide the quesetion in two parts 

left subtree and right subtree 

sum will be left + root.val + right 

what I need ? 

traversal ? 

dfs or bfs ? 

dfs can be for sum ? 

get a sum on every node with dfs 

use a dfs with sum carry per node 

left = 0 
right = 0

left + right + node.val 

if left is not None and right is not None:

	max_sum = (max_sum,curr_sum)


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Creating nodes for the tree
root = TreeNode(-10)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)

# Linking nodes to form the binary tree
root.left = node1
root.right = node2
node2.left = node3
node2.right = node4

# The tree looks like this:
#        -10
#        /  \
#       9    20
#             / \
#            15  7



class Solution():

	def helper_dfs(self,node):
		"""
		The helper function to make print dfs 
		"""

		if not node :

			return 

		#print the node value
		print(node.val)

		#make the recursive call on left and right
		self.helper_dfs(node.left)
		self.helper_dfs(node.right)


	def print_tree(self,root):
		"""
		The function to print the tree node 
		"""

		#constarints case
		if not root :

			return 0

		#make the recurive call
		self.helper_dfs(root)





class Solution_max():

	def __init__(self):

		self.max_sum = float("-inf")

	def helper_dfs(self,node,curr_sum):
		"""
		The function to get the carry sum as per dfs traversal

		"""

		#base case
		if not node :

			return 0

		#make the recursive call
		left = self.helper_dfs(node.left , curr_sum)
		right = self.helper_dfs(node.right, curr_sum)

		return node.val + left + right

	def maxPathSum(self,root):
		"""
		The function to find the max sum path 
		"""

		#constarints case 

		#one node 
		if not root.left and not root.right :

			return root.val

		#vars 
		curr_sum = 0 

		#make the helper dfs call
		#self.helper_dfs(root,curr_sum)

		#return the max sum
		return self.helper_dfs(root,curr_sum)



# The tree looks like this:
#        -10
#        /  \
#       9    20
#             / \
#            15  7


class Solution():

	def __init__(self):

		self.max_sum = float("-inf")

	def helper_dfs(self,node):
		"""
		The function to get the carry sum as per dfs traversal

		"""

		#base case
		if not node :

			return 0

		#make the left and right pass
		left = max(self.helper_dfs(node.left),0)
		right = max(self.helper_dfs(node.right),0)

		#make the current path sum
		curr_path_sum = left + right + node.val

		#update the max sum 
		self.max_sum = max(self.max_sum,curr_path_sum)

		return max(left,right) + node.val




	def maxPathSum(self,root):
		"""
		The function to find the max sum path 
		passes leetcode
		"""

		#constarints case 

		#one node 
		if not root.left and not root.right :

			return root.val

		#make the helper dfs call
		self.helper_dfs(root)

		#return the max sum
		return self.max_sum










sol = Solution()
print(sol.maxPathSum(root))