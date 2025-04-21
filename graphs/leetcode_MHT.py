"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. 
In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 
edges where edges[i] = [ai, bi] indicates that there is an undirected edge 
between the two nodes ai and bi in the tree, you can choose any node of the tree as the root.
 When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""



"""
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]


Constraints:

1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.



"""


"""
approach -- 

a dfs approach can give the height of the tree 
with tracked the height 

make graph 

we can do dfs on all the nodes 

we can have a dict of the height as key and root node as val 

sort and give out the least values 




"""
form collections import defaultdict


class Solution:

	def __init__(self):

		self.visited = set()
		self.graph = defaultdict(list)

	def _make_graph(self,edges) :
		"""
		The function to make the graph
		"""

		#traverse the edge list
		for u,v in edges :

			self.graph[u].append(v)
			self.graph[v].append(u)


	def _helper_dfs(self,node,height):
		"""
		The function to traverse the tree in dfs and get the height 
		"""

		#base case 
		if node in self.visited :

			return

		if 





    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    	"""
		The function to find the min height of the trees 
    	"""


