"""
The code is for graph exp and traversals 
"""

class Node:
	def __init__(self, val = 0, neighbors = None):
		self.val = val
		self.neighbors = neighbors if neighbors is not None else []





node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)



node1.neighbors = [node2,node4]
node2.neighbors = [node1,node3]
node3.neighbors = [node2,node4]
node4.neighbors = [node1,node3]




class Helper_Fun():

	def __init__(self):
		"""
		The function to make the res list
		"""

		self.node_set = set()
		self.res_lst  = []


	def graph_traversal_dfs(self,node):
		"""
		The graph traversal using dfs
		"""

		#base case 
		if not node:
			return []

		#traverse graph
		if node.val and node.val in self.node_set:

			return None

		#add in the main list
		self.res_lst.append(node.val)


		#add in the set 
		self.node_set.add(node.val)

		for neighbors in node.neighbors :

			self.graph_traversal_dfs(neighbors)


		return self.res_lst



	def graph_traversal_bfs(self,node):
		"""
		The graph traversal using dfs
		"""

		#base case
		if not node:
			return []

		#make the res lst 
		res_lst = []

		#make the visisted set 
		node_set = set()

		#make the queue:
		queue = [node]

		#start the traversal 

		while queue :

			temp_lst = []

			curr_node = queue.pop(0)

			if curr_node.val not in node_set :

				node_set.add(curr_node.val)

				res_lst.append(curr_node.val)

				for neighbors in curr_node.neighbors:

					if neighbors.val not in node_set:

						#temp_lst.append(neighbors.val)

						queue.append(neighbors)


		return res_lst




if __name__ == "__main__":

	helper_fun = Helper_Fun()
	print(helper_fun.graph_traversal_dfs(node1))
	print(helper_fun.graph_traversal_bfs(node1))



	
