"""
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). 
You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) 
to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles.
If it is not possible to find such walk return -1.
"""

"""
Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).


Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.

m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0
"""



"""

shortest path , must be bfs 

remove obstacle 

can remove and can not 

the calcluate the number of moves and keep the min moves 

if found the last point then get the moves 

a recursive decision tree for that ? 


_helper_bfs should be callable function 

_helper_dfs should be 


"""
from typing import List
from collections import deque





class Solution():
    """
    passes leetcode
    """
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        Find the shortest path from (0,0) to (m-1, n-1) with at most k obstacle eliminations.
        """
        # Edge case: If the grid is just one cell
        if len(grid) == 1 and len(grid[0]) == 1:

            return 0

        rows, cols = len(grid) -1  , len(grid[0]) - 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        # BFS Queue: (x, y, remaining k)
        queue = deque([(0, 0, k)])

        visited = set()

        visited.add((0, 0, k))

        steps = 0  # Number of steps taken

        # Start BFS traversal
        while queue:
            length_queue = len(queue)
            for _ in range(length_queue):

                x, y, remaining_k = queue.popleft()

                # Reached the target
                if x == rows and y == cols :

                    return steps

                # Explore all directions
                for dx, dy in directions:

                    new_x, new_y = x + dx, y + dy

                    # Boundary check
                    if 0 <= new_x <= rows and 0 <= new_y <= cols:

                        new_k = remaining_k - grid[new_x][new_y]  # Reduce k if obstacle

                        # Only proceed if we have enough k left and haven't visited this state
                        if new_k >= 0 and (new_x, new_y, new_k) not in visited:

                            queue.append((new_x, new_y, new_k))

                            visited.add((new_x, new_y, new_k))

            steps += 1  # Increment step count

        return -1  # If no path found






















