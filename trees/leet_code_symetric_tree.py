"""
find the symetric tree
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

	def isMirror(self,root1, root2):
		# If both trees are empty, then they are mirror images
		if root1 is None and root2 is None:
			return True

		if (root1 is not None and root2 is not None):
			if root1.val == root2.val:
				return (self.isMirror(root1.left, root2.right)and
						self.isMirror(root1.right, root2.left))
	
		# If none of the above conditions is true then root1
		# and root2 are not mirror images
		return False

	def isSymmetric(self,root):
	
		# Check if tree is mirror of itself
		return self.isMirror(root, root)
		


if __name__ == "__main__":
	sol = Solution()
	res = sol.isSymmetric(root)

	print(res)


		
		