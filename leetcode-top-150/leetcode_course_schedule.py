"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.


"""

"""

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.


Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.




"""

"""

aapproach -- 

using the traversal find the cycle 

not a graph 

no neighbors ? 



"""


#make graph testing 

numCourses = 4
prerequisites = [[0, 1], [1, 2]]

prerequisites2 = [[1, 0], [2, 1], [3, 2]]


def make_graph(prerequisites) : 
    """
    The function to make the graph 
    """

    graph = {}


    for edge in prerequisites:

        edge.reverse()

        for i in range(0,len(edge)) :

            if edge[i] not in graph:

                graph[edge[i]] = []

            else:

                graph[edge[i]].append(edge[i])

    return graph

           
print(make_graph(prerequisites))

