"""
merge the two binary tree, the merger is the sum of the tree in the place if not the node is none 
"""

"""
ideas to do it --- 

take start the traveral on both trees any order 
add both in the sane place and add up the value 
then make them add in same place
then traverse up

"""


class Solution():


	def treeTraversal(self,node):
		"""
		tree traverse system
		"""

		return tree.val


	def mergeTrees(self,node1,node2):
		"""
		the fubction to merge two trees

		"""

		if not node1 and not node2:

			return 0


		if not node1:

			return node2.val


		if not node2:

			return node1.val


		else:

			node.val = self.treeTraversal(node.left) + self.treeTraversal(node.right)


		

