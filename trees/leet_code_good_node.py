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

keep track of max value 
and iter down in the tree dfs with max tracking 
if the valus is greater than max increase the count 
keep a counter of the good nodes 

base case - 

if node.left is None and node.right is None:
	return [1,(node.val)]


"""



class Solution():

	def trackNode(self, node, max_val):
		"""
		Find the track of the node
		"""

		# base case 
		if not node:  # Corrected the case of 'Node' to 'node'
			return 0

		if node.left is None and node.right is None:
			return 1 if node.val >= max_val else 0  # Adjusted the return value

		res = 0 

		if node.val >= max_val:
			res = 1 

		max_val = max(max_val, node.val)

		# track the left and right node
		res += self.trackNode(node.left, max_val)
		res += self.trackNode(node.right, max_val)

		return res

	def goodNodes(self, node):
		"""
		The function to find the good node in the tree
		"""
		return self.trackNode(node, node.val)




if __name__ == "__main__":

	sol = Solution()

	res = sol.goodNodes(root)

	print(res)