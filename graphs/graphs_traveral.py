"""
traverse the graph in dfs and bfs manner 
"""

#make the graph 


graph = {
	"a":["b","d"],
	"b":[],
	"c":[],
	"d":["e","g"],
	"e":["c"],
	"f":[],
	"g":["f"]
}


class Solution():

	def dfs(self,graph,source):
		"""
		The function to do the dfs traversal in the graph 
		"""

		#initilaize the stack with a list
		stack = []

		#append the source 
		stack.append(source)

		#start the confition for empty stack
		while stack:
			#pop the node
			node = stack.pop(-1)
			print(node)

			for neighbour in graph[node]:
				stack.append(neighbour)


	def bfs(self,graph,source):
		"""
		The function to do the bfs of the graph
		"""

		#initilaize the queue
		queue = []

		#append in the queue
		queue.append(source)

		#start the condition for the empty stack
		while queue:
			#pop the node
			node = queue.pop(0)
			print(node)

			for neighbour in graph[node]:
				queue.append(neighbour)



if __name__ == "__main__":

	sol = Solution()

	res_dfs = sol.dfs(graph,"a")
	res_bfs = sol.bfs(graph,"a")

	print(res_dfs)
	print(res_bfs)

