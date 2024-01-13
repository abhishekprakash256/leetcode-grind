"""
find if the binary tree is balanced , the left or the right tree not differ by 1

"""

from tree_helper import Helper

class Node:

	def __init__(self,val):

		self.left = None
		self.right = None
		self.val = val


#------------------- test casese -------------------

#balanced tree
#make the nodes 

root = Node(3)
node1 = Node(9)
node2 = Node(20)
node3 = Node(15)
node4 = Node(7)

#connect the node

root.left = node1
root.right = node2
node2.left = node3
node2.right = node4



#unblalanced tree

root2 = Node(3)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)


root2.left = node5
node5.left = node6
node6.left = node7



class Solution():

	def find_height(self,node):
		"""
		The function to find the height of the tree
		"""
		if node is None:
			return 0 

		else:

			return max(self.find_height(node.left),self.find_height(node.right)) +1


	def balancedTree(self,node):

		"""
		the function to find if the tree is balanced or not 
		the max diff in left and right subtree should be 1
		"""

		if node is None:
			return True


		lh = self.balancedTree(node.left)
		rh = self.balancedTree(node.right)

		if abs((lh - rh) <=1) and self.balancedTree(node.left) is True and self.balancedTree(node.right) is True:

			return True

		return False 

			


if __name__ == "__main__":

	helper = Helper()

	#helper.printTree(root)
	#helper.printTree(root2)


	sol = Solution()
	height = sol.find_height(root)
	bal = sol.balancedTree(root)

	print(height)
	print(bal)



