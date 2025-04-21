"""
Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. You are only allowed to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given an integer n and a helper function bool knows(a, b) that tells you whether a knows b. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.

Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.

Note that the n x n 2D array graph given as input is not directly available to you, and instead only accessible through the helper function knows. graph[i][j] == 1 represents person i knows person j, wherease graph[i][j] == 0 represents person j does not know person i.

 

"""

"""
Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1
 means person i knows person j, otherwise graph[i][j] = 0 means person i
  does not know person j. The celebrity is the person labeled as 1 because 
  both 0 and 2 know him but 1 does not know anybody.



Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.

"""


"""
approach -- 

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

knows(a,b) then I will know true or false 

[0,1]
n = 2 
0->1 , 1 
1->0 , 0
0 . 1 , -1 



[0,1,2]

0,1 -> T 
1,0 -> F
0,2 -> T
2,0 -> T
1,2 -> F
2,1 -> T

make combinations through recursion 

ask the question from bool and make edges of only the T ones 

(0,1)-> T , (0,2) -> T , (2,0) -> T , (2,1) -> T

also 1 should not know any of those 
simple never in key 
{0:[1,2], , 2:[0,1] }

make freq table ? 

{ 0 : 1 , 2 : 0 , 1 : 2 } in degree 



have max out degree and 0 in degree



check who comes on most second position and then taht's the celebrity 

if all equal then return -1 

"""

# def knows(a: int, b: int) -> bool:


from collections import defaultdict


class Solution_wrong():

    def __init__(self):

        self.combinations = []
        self.graph = defaultdict(list)

    def make_combinations(self,temp_lst):
        """
        The function to make the combinations of pairs
        """

        #base case if two length is found 
        if len(temp_lst) == 2 :

            self.combinations.append(temp_lst)

            return

        #make the recursive calls 
        for i in range(self.n) :

            if i not in temp_lst :

                self.make_combinations(temp_lst + [i])



    def make_graph(self,pair_list):
        """
        The function to make the graph by using the know api calls 
        """

        #iterate on the pairs
        for a , b in pair_list :

            if knows(a,b) : #use the know function api

                self.graph[a].append(b)


    def find_max_indegree_zero_outdegree(self):
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        # Initialize all nodes in in-degree and out-degree
        for node in self.graph:
            in_degree[node] = 0  # Ensure all nodes are in dictionary
            out_degree[node] = 0

        # Calculate in-degree and out-degree
        for node in self.graph:
            out_degree[node] = len(self.graph[node])  # Out-degree = number of outgoing edges
            for neighbor in self.graph[node]:
                in_degree[neighbor] += 1  # Increment in-degree for the target node

        # Find the node with max in-degree and zero out-degree
        max_in_degree_node = None
        max_in_degree = -1

        for node in in_degree:
            if out_degree[node] == 0 and in_degree[node] > max_in_degree:
                max_in_degree = in_degree[node]
                max_in_degree_node = node

        return max_in_degree_node


    def findCelebrity(self, n: int) -> int:
        """
        The function to find the celebity and return -1 if none 
        """
        self.n = n

        #constarints case 
        if n == 1 :

            return -1

        #make the temp list
        temp_lst = []

        #make the combinations
        self.make_combinations(temp_lst)

        #make the graph
        self.make_graph(self.combinations)

        #iterate the graph and retrun the max edge
        return self.find_max_indegree_zero_outdegree()



class Solution_slow:

    def is_celebrity(self, i):

        for j in range(self.n):

            if i == j:

                continue # Don't ask if they know themselves.
            
            if knows(i, j) or not knows(j, i):

                return False

        return True

    def findCelebrity(self, n: int) -> int:
        self.n = n

        for i in range(n):

            if self.is_celebrity(i):
                
                return i
        
        return -1
    


class Solution:
    """
    passes leetcode
    """
    def findCelebrity(self, n: int) -> int:
        candidate = 0  # Assume the first person is the celebrity
        
        # First pass: Find the potential celebrity
        for i in range(1, n):
            if knows(candidate, i):  
                candidate = i  # If candidate knows i, then candidate is not a celebrity, i might be
        
        # Second pass: Verify the candidate
        for i in range(n):
            if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
                return -1  # Not a celebrity
        
        return candidate





class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        The function to make find the celebrity 
        """

        pass











































































