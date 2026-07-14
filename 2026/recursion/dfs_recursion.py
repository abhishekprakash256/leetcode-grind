"""
the tree recuriosn to print the nodes
"""

class Node():

	def __init__(self,val):

		self.val = val
		self.left = None
		self.right = None



#make the nodes 
root = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)
seventh = Node(7)


#connect the node 
root.left = second
root.right = third
second.left = fourth
second.right = fifth
third.left = sixth
third.right = seventh




class TreeHelper():

	def dfs(self,node) :
		"""
		The function to print the node the tree
		"""

		if not node:

			return 

		print(node.val)

		if node.val :

			self.dfs(node.left)

			self.dfs(node.right)




tree_helper = TreeHelper()

res = tree_helper.dfs(root)

print(res)
