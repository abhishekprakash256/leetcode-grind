"""
make the basic tree
"""

#make the tree node and connect them


class node:

	def __init__(self,val):

		self.left = None
		self.right = None
		self.val = val



#make the tree

root = node(3)
node1 = node(9)
node2 = node(20)
node3 = node(15)
node4 = node(7)


#connect the node 
root.left = node1
root.right = node2
node2.left = node3
node2.right = node4


#wrong solution 

class Solution:
	def maxDepth(self, root) -> int:
		"""
		find the max depth of the tree
		"""

		if root is None : 

			return 0 

		elif root.left :

			return self.maxDepth(root.left) + 1

		elif root.right:

			return self.maxDepth(root.right) + 1

		else:

			return self.maxDepth(root.left) + self.maxDepth(root.right)

			

	def maxDepth2(self,node):
		
		if node is None:
			return 0
	 
		else:
	 
			# Compute the depth of each subtree
			lDepth = self.maxDepth2(node.left)
			rDepth = self.maxDepth2(node.right)
	 
			# Use the larger one
			if (lDepth > rDepth):
				return lDepth+1
			else:
				return rDepth+1



if __name__ == '__main__':
	sol = Solution()

	res = sol.maxDepth2(root)

	print(res)


