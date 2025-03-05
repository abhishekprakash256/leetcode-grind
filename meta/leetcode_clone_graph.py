"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
"""


"""

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).



Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.


The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100

"""


"""

approach -- 

make a grph first then 

then copy it using the bfs 

make a node and create the copy 

"""


from collections import deque


class Solution():

    def __init__(self):

        self.clone_graph = {}



    def cloneGraph(self,node):
        """
        The function to make the clone graph usinhg bfs 
        """

        #constraints case

        #no node
        if not node :

            return None

        #only one node 
        if node.neighbors is None :

            return Node(node.val)


        # Clone the first node and store it in the hashmap
        self.clone_graph[node] = Node(node.val)

        #make the queue
        queue = deque([node])

        #start the itertaion
        while queue :

            original_node = queue.popleft()

            for neighbor in original_node.neighbors :

                if neighbor not in self.clone_graph :

                    #make the mapping 
                    self.clone_graph[neighbor] = Node(neighbor.val)

                    #make the copy node 
                    queue.append(neighbor)

                self.clone_graph[original_node].neighbors.append(self.clone_graph[neighbor])

        return self.clone_graph[node]





