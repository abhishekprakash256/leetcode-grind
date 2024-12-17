"""
You are given the root of a binary tree with n nodes, 
where each node is uniquely assigned a value from 1 to n. You are also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.

"""


"""

Input: root = [1,2], voyage = [2,1]
Output: [-1]
Explanation: It is impossible to flip the nodes such that the pre-order traversal matches voyage.


Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]
Explanation: Flipping node 1 swaps nodes 2 and 3, so the pre-order traversal matches voyage.

"""



"""
approach -- 

do the dfs traversal in the pre order 
then make a dst based on the chnages 
using recursion 
then change the roots and traverse and draw the tree again
and match the list till it comes up




"""




class Solution:

	def __init__(self):

		self.count = 0 


	def dfs_traversal(self, node, res_lst):
		"""
		Perform preorder traversal and append node values to res_lst.
		"""
		# base case
		if not node:
			return

		# Add the current node value
		res_lst.append(node.val)

		# Traverse left
		self.dfs_traversal(node.left, res_lst)

		# Traverse right
		self.dfs_traversal(node.right, res_lst)

		return res_lst




	def flip_tree(self,node):
		"""
		The function to flip the node of the tree
		"""

		#base case 
		if not node:
			return None
		
		#check the tree match 

		res_lst = self.dfs_traversal(self.root,res_lst= [])

		#match the traversal 
		if res_lst == self.voyage :

			return [self.count]

		
		#flip the node
		node.left , node.right = node.right , node.left
		
		#incraese the count if flipped 
		self.count += 1 


		#make the recursive traversal calls
		self.flip_tree(node.left)
		self.flip_tree(node.right)


		#the last case if both node ends :
		if self.count > len(self.voyage) and not node.left and not node.right and res_lst != self.voyage: 
			return [-1]



	def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
		"""
		The function to make the flip match the tree
		"""
		self.root = root
		self.voyage = voyage

		# the base case 	
		if not root:
			return []
		
		# base case for no flip needed
		res_lst = self.dfs_traversal(self.root, res_lst=[])

		if res_lst == voyage:
			return []

		# make the flip and match 
		self.flip_tree(self.root)




		

























