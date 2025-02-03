"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}


"""


"""

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

"""


"""

approach -- 

make the graph in the dict format and traverse the graph

using dfs use a vsisted and check if the ndoe is there 

"""



# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution_wrong():

    def __init__(self):

        self.visited = set() #the visited set 

        #self.dummy = Node(self.node.val) #make the dummy node as new head


    def helper_dfs(self,node,new_node) :
        """
        The helper function to do dfs and make graph
        """

        #base case 

        #no neighbors 
        if not node.neighbors : 

            return None

        #add in the visited 
        self.visited.add(node.val)

        #make the traversal
        for neighbor in node.neighbors :

            if neighbor.val not in self.visited :

                #connect the nodes
                new_node.neighbors = neighbor

                #make the new node 
                new_node = Node(neighbor.val)

                self.helper_dfs(neighbor , new_node)

                self.visited.add(neighbor.val)




    def cloneGraph(self, node ) :
        """
        The function to clone the graph using dfs
        """

        self.node = node

        #constarint case 

        #no node 
        if not node :

            return None

        #one node 
        if node.neighbors is None : 

            return Node(node.val)

        #make the new node 
        new_node = Node(node.val)

        #make the graph with recursive calls 
        self.helper_dfs(node, new_node )

        return new_node



# make the graph 
# Creating a simple graph
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]



class Helper_Fun():

    def __init__(self):

        self.visited = set()

    def helper_dfs(self, node) :
        """
        The function to print the graph
        """
        #base case 
        if not node.neighbors :

            return None

        print(node.val)

        #add the node in visited
        self.visited.add(node.val)

        #print the graph
        for neighbor in node.neighbors : 

            if neighbor.val not in self.visited :
                
                self.helper_dfs(neighbor)


    def print_graph_dfs(self,node):
        """
        The function to print the graph using dfs
        """

        #constraints case

        #no node 
        if not node :

            return None


        if node.neighbors is None :

            return node.val

        #make the recursive graph calls
        self.helper_dfs(node)



helper_fun = Helper_Fun()

print(helper_fun.print_graph_dfs(node1))



























