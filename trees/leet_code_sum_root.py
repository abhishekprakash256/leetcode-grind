"""
leet code find the sum of the root ot leaf node
find the sum of the root node from the left and right 
we add and make a two digit number then we add them together 
Example 
-----

		8
	   / \
	  7   4

87 + 84 = 171

		4
	   / \
	  9   0
	 / \
	5   1


495 + 491 = 1026

		
			7
		   / \
		  4   6
		 / \ / \
		1   1 1  1


741 + 741 + 761 + 761 = 

"""


"""
The methedelogy as follows - 


#base case 
if not node: 
	return 0 


#make the digit 

left_val = node.val* 10 + node.left.val 
right_val = node.val*10 + node.right.val

full sum 

node_sum = left_val + right_val


two function , using recursion --- 



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

root = Node(4)
node1 = Node(9)
node2 = Node(5)
node3 = Node(1)
node4 = Node(0)




#make the tree

root.left = node1
root.right = node4
node1.left = node2
node2.right = node3




class Solution():

	def traverse_node(self,node):
		"""
		Helper function to append the list
		"""

		if node:

			print(node.val)

			self.traverse_node(node.left)

			self.traverse_node(node.right)


	













if __name__ == "__main__":

	#helper = Helper()

	#helper.printTree(root)

	sol = Solution()

	res = sol.traverse_node(root)

	print(res)










