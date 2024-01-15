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

			return None

		v1 = node1.val if node1 else 0 
		v2 = node2.val if node2 else 0 

		node = Node(v1 + v2)

		node.left = self.mergeTrees(node1.left is node1 else None, node2.left if node2 else None)
		node,right = self.mergeTrees(node1.right is node1 else None, node2.right if node2 else None)

		return node
		