"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. 
There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.
"""

"""

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1

Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

Constraints:

    n == grid.length == grid[i].length
    2 <= n <= 100
    grid[i][j] is either 0 or 1.
    There are exactly two islands in grid.



"""

"""


The grid is the connection of the 1's that connect to each other vertically or horniontally 

1 Find the islands 
2. Find the bridge 

1. Find the island  - 

- find the 1 and make bfs search on the traversal to identify the islnd 
move the up and down and can make an island we can keep the count of the 1's 


first find the one of the island then go to the last -- 

when the chnage of the number comes look for another 1 and explore to find the shgortest path using bfs 

we can find the island and exhaust the last points all end coordiantes 

find the other island and store the cooreduinates 

start the search from the end to other end using BFS 


sudo code 

first_islnad_edge = []
second_island_edge = [] 


def dfs(i,j,edge_lst):

    all edge cond 
    
    if 






count = 0 

for i in range row:

    for j in range col :

        if matix[i][j] == 1 :

            first_island_edges.append([i,j])
            self.dfs(i,j , first_island_edges)

            count += 1 




"""