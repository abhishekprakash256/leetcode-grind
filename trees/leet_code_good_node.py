"""
find the good node in a tree 
the node is the node that has no value less than that in the path 
"""




from tree_helper import Helper

class Node:

	def __init__(self,val):

		self.left = None
		self.right = None
		self.val = val






#make the first tree
root = Node(3)
node1 = Node(1)
node2 = Node(4)
node3 = Node(3)
node4 = Node(1)
node5 = Node(5)


#connect the nodes of trees
root.left = node1
root.right = node2
node1.left = node3
node2.left = node4
node2.right = node5

out = 4


#make second tree
root2 = Node(3)
node6 = Node(3)
node7 = Node(4)
node8 = Node(2)


#make the tree 2 
root2.left = node6
node6.left = node7
node6.right = node8



"""
		1
		/ \
	   3   4
	  / \
     6   2

out = 4

"""



 class Solution():

 	def goodNodes(self,node):

 		"""
		The function to find the good node in the tree
 		"""

 		pass
