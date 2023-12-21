"""
make the inorder traversal of the tree
"""

class node:
	def __init__(self,val):

		self.left = None
		self.right = None
		self.val = val


#make the tree

root = node(1)
node1 = node(2)
node2 = node(2)
node3 = node(3)
node4 = node(3)
node5 = node(4)
node6 = node(4)

#join the node 

root.left = node1
root.right = node2
node1.left = node3
node1.right = node5
node2.left = node4
node2.right = node6



class Solution:
    def levelOrder(self, root):
        """
        The function to level order traversing
        node -> left -> right
        """

        