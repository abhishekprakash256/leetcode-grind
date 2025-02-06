"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""


"""

Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the 
root is the node with label 1 which is the only MHT.


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]

"""

"""
approach -- 

make graph 

{1 : [0,2,3] } -> 1 

{ 3 : [0,1,2,4] , 5 : [4] }

number of keys ? 

do a height dfs traversal ? 


Constraints:

1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.


"""


from collections import defaultdict

class Solution_wrong:

    def __init__(self):

        self.graph = defaultdict(list)
        self.result = []


    def make_graph(self, edges ) :
        """
        The function to make the graph
        """

        for a ,b in edges :

            self.graph[a].append(b)
            self.graph[b].append(a)


    def findMinHeightTrees(self, n, edges) :
        """
        The function to find the min height tree that can be formed
        """

        #constraints case
        if n == 0 :

            return 1 

        #make graph 
        self.make_graph(edges)

        #return the length of the graph that will be min height
        return self.graph




class Solution():

    def __init__(self):

        self.graph = defaultdict(list)
        self.result = []

    def make_graph(self,edges):
        """
        The function to make the graph 
        """

        #make the graph 
        for a , b in edges :

            self.graph[a].append(b)
            self.graph[b].append(a)
        


    def make_tree(self):
        """
        The function to make the trees
        """

        pass



    def findMinHeightTrees(self, n, edges) :
        """
        The function to find the node of the min tree
        """

        #base case

        #if there is only one node 
        if len(edges[0]) == 1 :

            return [edges[0][0]]

        #make the graph 
        self.make_graph(edges)

        #case with only one key node 
        if len(self.graph) == 1 :

            #return the first element in the graph
            return [self.grap.item(0)]

        







n = 4 
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

sol = Solution()

print(sol.findMinHeightTrees(n, edges))