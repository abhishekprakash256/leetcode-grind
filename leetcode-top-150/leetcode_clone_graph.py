"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.
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

"""


"""
approach - 

dfs make a node and traverse and add neighbors 
base case 
if not node:
	return []

if node.neighbors is None:
	return [[]]


class Solution:
	def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


queue = [node]

visisted = set()


while queue:

	curr_node = queue.pop(0)

	temp_node = Node(node.val)

	if curr_node.val not in visited:

		temp_node = Node(node.val)

		for neighbors in curr_node.neighbors:

			queue.append(neigbors)

			temp_node.neighbors = Node(neighbors.val)


"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution2:
    def cloneGraph(self, node):
        """
        Clones a graph using BFS.
        """
        if not node:
            return None
        
        # A mapping from original node to its clone
        clone_map = {}

        # Initialize the queue with the original node
        queue = [node]
        
        # Clone the first node and add it to the map
        clone_map[node] = Node(node.val)

        while queue:
            # Pop the current node from the queue
            curr_node = queue.pop(0)
            
            # Traverse all its neighbors
            for neighbor in curr_node.neighbors:
                if neighbor not in clone_map:
                    # Clone the neighbor and add it to the map
                    clone_map[neighbor] = Node(neighbor.val)
                    # Add the original neighbor to the queue
                    queue.append(neighbor)
                
                # Link the current node's clone to the neighbor's clone
                clone_map[curr_node].neighbors.append(clone_map[neighbor])
        
        # Return the clone of the input node
        return clone_map[node]




class Solution3:
    def cloneGraph(self, node):
        if not node:
            return None

        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]

            # Clone the current node
            clone = Node(node.val)
            visited[node] = clone

            # Clone all neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)



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


class Solution4:

    def __init__(self):

        self.visited = {}
        self.res_lst = []


    def dfs_graph(self,node):
        """
        The dfs graph traversal 
        """

        #base case 
        if node in self.visited:
            return

        #add the node in visited
        self.visited[node] = True

        #add the ndoe in result list 
        self.res_lst.append(node.val)

        for nodes in node.neighbors:

            self.dfs_graph(nodes)


        return self.res_lst


    def bfs_graph(self,node):
        """
        The bfs traverdal of the graph 
        """

        #base case 
        if not node :
            return []

        #only one node 
        if not node.neighbors : 
            return [node]

        #make the visisted dict 
        visited = {}

        #make the result list 
        res_lst = []

        #make the queue
        queue = [node]

        #start the traversal 
        while queue : 

            curr_node = queue.pop(0)

            if curr_node.val not in visited:

                #add the node in visited 
                visited[curr_node.val] = True

                #add to the result list 
                res_lst.append(curr_node.val)


                for neighbor in curr_node.neighbors:

                    if neighbor.val not in visited:

                        queue.append(neighbor)

        return res_lst






class Solution():

    def __init__(self):

        self.visited = {}


    def cloneGraph(self,node):
        """
        The function to clone the graph using bfs
        """

        #base case 
        if not node :
            return []

        #only one node 
        if not node.neighbors : 
            return [node]

        #make the visisted dict 
        visited = {}

        #make the queue
        queue = [node]

        #start the traversal 
        while queue:

            curr_node = queue.pop(0)

            if curr_node.val not in visited:

                new_node = Node(curr_node.val)

                visited[curr_node.val] = True

                #explore all the neighbors 
                for neighbor in curr_node.neighbors :

                    if curr_node.val not in visited:

                        curr_node.neighbors = neighbor

                        queue.append(curr_node)



#understand this 


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        """
        Clones a graph using BFS.
        """
        # Base case: If the input node is None, return None
        if not node:
            return None

        # Dictionary to store visited nodes and their clones
        visited = {}

        # Create the clone of the starting node
        visited[node] = Node(node.val)

        # BFS queue initialized with the original node
        queue = [node]

        while queue:
            curr_node = queue.pop(0)

            # Iterate through all neighbors
            for neighbor in curr_node.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and add to visited
                    visited[neighbor] = Node(neighbor.val)
                    # Add the original neighbor to the queue
                    queue.append(neighbor)
                
                # Link the clone of the current node to the clone of the neighbor
                visited[curr_node].neighbors.append(visited[neighbor])

        # Return the clone of the original input node
        return visited[node]






if __name__ == "__main__":

    sol = Solution4()
    print(sol.dfs_graph(node1))
    print(sol.bfs_graph(node1))
