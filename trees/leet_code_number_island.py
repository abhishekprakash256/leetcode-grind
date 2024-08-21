"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

"""


"""
approach

use the dfs recusively to eexploare all the brnahces horizontal and verttical 
make the toched node as 0 
traverse all the points till end of the materix 
mantain a counter for island


"""