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
{0:1, 0:2 , 2:0 , 2:1 }

find the max indegree ? and 0 out degree is degree the number of neighbor ?



check who comes on most second position and then taht's the celebrity 

if all equal then return -1 

"""

# def knows(a: int, b: int) -> bool:

from collections import defaultdict

class Solution():

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

                self.helper_dfs(temp_lst + [i])



    def make_graph(self,pair_list):
        """
        The function to make the graph by using the know api calls 
        """

        #iterate on the pairs
        for a , b in pair_list :

            if knows(a,b) : #use the know function api

                self.graph[a] = b 
      

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
        for i in range(n):

            self.make_combinations(temp_lst)

        #make the graph
        self.make_graph(self.result)

        #iterate the graph and retrun the max edge 






