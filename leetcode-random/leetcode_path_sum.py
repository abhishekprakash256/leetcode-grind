"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all 
the values along the path equals targetSum.

A leaf is a node with no children.
"""


"""
example 1 

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.


example 2
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


The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000



"""


"""

approach using dfs 

we add the vales and carry it add the both parts and match if equal 

using a helper_dfs

if left + right == target 

return true 

pass the sum + if node.val add the val



"""




class Solution():

	def helper_dfs(self,node, curr_sum):
		"""
		The function to calculate the sum and match
		passes leetcode
		"""
		#base case

		#if node is false
		if not node:

			return False

		#add the sum 
		curr_sum += node.val

		#equal case 
		if node.left is None and node.right is None:

			return cur_sum == self.targetSum

		#make the recursion call
		return self.helper_dfs(node.left,curr_sum) or self.helper_dfs(node.right, curr_sum)




	def hasPathSum(self,root, targetSum) :
		"""
		The function to find the target sum if that exists in the tree
		"""

		self.targetSum = targetSum

		#constarint case

		#if not node
		if not root:

			return False


		return self.helper_dfs(root,0)