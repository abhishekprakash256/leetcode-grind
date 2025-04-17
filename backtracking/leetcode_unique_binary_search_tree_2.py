"""
Given an integer n, return all the structurally unique BST's (binary search trees), 
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
"""


"""

Example 1:

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:

Input: n = 1
Output: [[1]]

 

Constraints:

1 <= n <= 8

"""


"""

apprroch -- 

using a recurisive dfs soln to make tree 

helper traversal functuin to check the base case and then append the tree 

make a tree class as well and add the nodes 

have a head and if then add the other left or right 

have the decision to left and right 

either can go null


"""


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution():

	def __init__(self):

		self.results = []


	def _make_tree(self,node_val):
		"""
		The function to make the tree
		"""

		node = TreeNode(node_val)

		if not head :

			self.head = node



	def _counter_helper(self,node, count)
		"""
		The function to make the helper counter
		"""

		if not node :

			return

		if node.left :	

			count +=1
			self._counter_helper(node.left, count)


		if node.right :

			count += 1 
			self._counter_helper(node.right, count) :




	def _nodes_count(self,head):
		"""
		The function to count the number of nodes in the tree
		"""
		#vars
		temp = node

		count = 0 

		self._counter_helper(head,count)

		return count





	def _helper_dfs(self,curr_node,left_node,right_node):
		"""
		The function to do the helper dfs calls for making tree
		"""

		#base case 

		if self._nodes_count(curr_node) == self.n :

			self.results.append()

		




    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
    	"""
		The function to make the possible trees
    	"""

    	self.n = n 

    	pass
















