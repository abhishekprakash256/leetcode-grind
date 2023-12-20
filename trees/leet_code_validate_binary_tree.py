"""
leet code to find the tree is valid or not 
"""


class node:
	def __init__(self,val):

		self.left = None
		self.right = None
		self.val = val



#make the tree

root = node(2)
node1 = node(1)
node2 = node(3)



#connect the node 
root.left = node1
root.right = node2

#make the tree
root2 = node(5)
node3 = node(1)
node4 = node(4)
node5 = node(3)
node6 = node(6)


#connect the node 
root2.left = node3
root2.right = node4
node4.left = node5
node5.left = node6


class Solution:
	def isValidBST_incorrect(self, node) -> bool:
		"""
		find the tree is valid or not 
		"""

		if node is None:
			return True

		else:

			left_val = self.isValidBST(node.left)
			right_val = self.isValidBST(node.right)

			if left_val.val <= node.val <=right_val.val:
				return True

			else:
				return False 

	
	def isValidBST(self,node):
		"""
		check if the tree is valid bst or not 
		"""

		return self.isBSTHelper(node,float('-inf'), float('inf'))

	def isBSTHelper(self,node,min_val, max_val):

		if node is None:
			return True

		if not (min_val < node.val < max_val):
			return False

		return self.isBSTHelper(node.left, min_val,node.val) and self.isBSTHelper(node.right,node.val,max_val)




if __name__ == "__main__":

	sol = Solution()
	res = sol.isValidBST(root)

	print(res)





