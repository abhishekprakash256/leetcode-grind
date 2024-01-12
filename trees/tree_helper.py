"""
methods to help print the tree
"""

class Helper():

	#print the tree in order root ,left, right
	def printTree(self,node):

		if node:

			print(node.val)

			self.printTree(node.left)

			self.printTree(node.right)

