"""
the function to find the path in the graph if that is visisted or not as the graph is ascylic
"""

graph = {
	"a": ["b","c"],
	"b":["a","f","d"],
	"c":["a"],
	"d":["b","g","i"],
	"e":["f","h"],
	"f":["b","e"],
	"g":["d","h"],
	"h":["e","g"],
	"i":["d"]
}





class Solution():

	def dfs(self,src,dest,graph, vis = set()):
		"""
		The function to find if src and destination can be reach 
		"""

		#base case 
		if src == dest :
			return True 

		#store the node 
		vis.add(src)

		#make a dummy answer
		ans = False

		for neighbour in graph[src]:

			if neighbour not in vis:
				ans = ans or self.dfs(neighbour,dest,graph,vis)

		return ans



if __name__ == "__main__":

	sol = Solution()

	res = sol.dfs("a","g",graph)


	print(res)