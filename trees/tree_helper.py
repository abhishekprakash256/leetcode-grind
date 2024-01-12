"""
methods to help print the tree
"""

class Helper():

	#print the tree in order root ,left, right
	def printTree(self,node):

		if node:

			self.printTree(node.left)

			print(node.val)

			self.printTree(node.right)

