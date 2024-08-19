"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
"""


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
"""

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

		
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Example binary tree
#          1
#        /   \
#       2     3
#      / \   / \
#     4   5 6   7


"""
appach 

1.  using the queue for traversal 
	flip the traversal as per iinsertion of the values 
	make a small list and append on it 
	make a flip vars
	alternate the flip var as per condition
	
"""



class Solution():
	def bfs(self,node):
		"""
		The function to make the bfs 
		"""
		#base case
		if not node:
			return []
	
		#vars
		queue = [node]
		node_lst = []

		while queue:

			curr_node = queue.pop(0)
			node_lst.append(curr_node.val)

			if curr_node.left:
				queue.append(curr_node.left)
			
			if curr_node.right:
				queue.append(curr_node.right)
		
		return node_lst
	
	
	def bfs_list(self,node):
		"""
		The function to make the bfs 
		"""
		#base case
		if not node:
			return []
	
		#vars
		queue = [node]
		node_lst = []

		while queue:

			temp_lst = []

			for i in range(len(queue)):

				curr_node = queue.pop(0)

				temp_lst.append(curr_node.val)

				if curr_node.left:
					queue.append(curr_node.left)
				
				if curr_node.right:
					queue.append(curr_node.right)
			
			node_lst.append(temp_lst)
		
		return node_lst


	def bfs_reversed_list(self,node):
		"""
		The function to make the bfs 
		The code passed leet code 
		"""
		#base case
		if not node:
			return []
	
		#vars
		queue = [node]
		node_lst = []
		flip = True

		while queue:

			temp_lst = []

			for _ in range(len(queue)):

				curr_node = queue.pop(0)

				temp_lst.append(curr_node.val)

				if curr_node.left:
					queue.append(curr_node.left)
				
				if curr_node.right:
					queue.append(curr_node.right)

			
			if not flip:
				temp_lst.reverse()
				flip = True

			else:
				flip = False


			node_lst.append(temp_lst)
		
		return node_lst



	def zigzagLevelOrder(self, node: Optional[TreeNode]) -> List[List[int]]:
		"""
		The function to make the bfs 
		"""
		#base case
		if not node:
			return []
	
		#vars
		queue = [node]
		node_lst = []
		flip = True

		while queue:

			temp_lst = []

			for _ in range(len(queue)):

				curr_node = queue.pop(0)

				temp_lst.append(curr_node.val)

				if curr_node.left:
					queue.append(curr_node.left)
				
				if curr_node.right:
					queue.append(curr_node.right)

			
			if not flip:
				temp_lst.reverse()
				flip = True

			else:
				flip = False


			node_lst.append(temp_lst)
		
		return node_lst

if __name__ == "__main__":

	sol = Solution()
	print(sol.bfs(root))
	print(sol.bfs_list(root))
	print(sol.bfs_reversed_list(root))


	


