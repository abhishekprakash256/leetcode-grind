"""

Playing with trees
"""

class Node:

	def __init__(self,val = None, left = None, right = None , next = None):

		self.val = val
		self.left = left
		self.right = right
		self.next = next



#make node 

root = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)
node5 = Node(7)


#connect the trees

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.right = node5




class TreeHelper():
	
	def dfs_tree(self,node):
		"""
		To dfs traverse the tree
		""" 

		if node:

			print(node.val)

			self.dfs_tree(node.left)
			self.dfs_tree(node.right)



	def bfs_tree(self,node):
		"""
		The function to print the tree node in bfs traversal
		"""

		#base case 
		if not node:
			return []


		#make the queue :
		queue = [node]
		res_lst = []


		while queue:

			curr_node = queue.pop(0)


			if curr_node :

				res_lst.append(curr_node.val)

				queue.append(curr_node.left)
				queue.append(curr_node.right)

		return res_lst

	def bfs_tree_level(self,node):
		"""
		The function to append the node per level
		"""

		#base case 
		if not node:
			return [[]]

		#make the queue 
		queue = [node]

		#make the result list 
		res_lst = []


		while queue:

			temp_lst = []

			for _ in range(len(queue)):

				temp_node = queue.pop(0)

				if temp_node:

					temp_lst.append(temp_node.val)

					queue.append(temp_node.left)

					queue.append(temp_node.right)

			res_lst.append(temp_lst)


		return res_lst









if __name__ == '__main__':
	
	treehelper = TreeHelper()

	print(treehelper.dfs_tree(root))

	print(treehelper.bfs_tree(root))

	print(treehelper.bfs_tree_level(root))