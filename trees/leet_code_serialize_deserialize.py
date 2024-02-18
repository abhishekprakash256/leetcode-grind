"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. 

There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, 
so please be creative and come up with different approaches yourself.


"""



"""

Algo ---

traversal algorithm -- 


def serilization():
	
	# base case 
	if not node:
		return []

	if node.left is None and node.right is None:
		return return [node]

	queue = [node]
	res_lst = []

	
	while queue:

		node = queue.pop(0)
		
		res_lst.appen(node.val)

		if node.left:
			queue.append(node.left)

		if node.right:
			queue.append(node.right)
		

	return res_lst













"""







# Example binary tree
#          1
#        /   \
#       2     3
#      / \   / \
#           6   7
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

		
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)





class Solution():

	def serilization(self,node):
		"""
		The function to make the data for the tree
		"""

		#base case 
		if not node:
			return []

		#base case 
		if node.left is None and node.right is None:
			return [node]

		res_lst = []
		queue = [node]

		while queue:


			node = queue.pop(0)

			if node :
				res_lst.append(node.val)
				queue.append(node.left)
				queue.append(node.right)
			else:
				res_lst.append(None)

		return res_lst


		def deserialize(self, data):
			"""
			The function to make the tree from data
			"""

			pass







if __name__ == "__main__":

	sol = Solution()

	res = sol.serilization(root)

	print(res)






