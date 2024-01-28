"""
check if the path exist between the source and destination 
return True or False if the path exists for not
"""

#make the graph 

graph = {
	"a":["b","c"],
	"b":["f","d"],
	"c":[],
	"d":["g","i"],
	"e":["h"],
	"f":["e"],
	"g":["h"],
	"h":[],
	"i":[]
}




#test cases 

src, dest = "a", "h"

src2, dest2 = "f","a"



class Solution():

	def hasPath(self,source,destination,graph):
		"""
		The function to find the path dest to src
		"""

		if source == destination:
			return True

		ans = False

		for node in graph[source]:
			ans = ans or self.hasPath(node,destination,graph)


		return ans

		

if __name__ == "__main__":

	sol = Solution()

	res = sol.hasPath(src,dest,graph)

	res2 = sol.hasPath(src2,dest2,graph)

	print(res)

	print(res2)