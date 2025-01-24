"""

You will be given a square chess board with one queen and a number of obstacles placed on it. Determine how many squares the queen can attack.

A queen is standing on an
chessboard. The chess board's rows are numbered from to , going from bottom to top. Its columns are numbered from to , going from left to right. Each square is referenced by a tuple, , describing the row, , and column,

, where the square is located.

The queen is standing at position
. In a single move, she can attack any square in any of the eight directions (left, right, up, down, and the four diagonals). In the diagram below, the green circles denote all the cells the queen can attack from : 
"""


"""

 int n: the number of rows and columns in the board
- nt k: the number of obstacles on the board
- int r_q: the row number of the queen's position
- int c_q: the column number of the queen's position
- int obstacles[k][2]: each element is an array of integers, the row and column of an obstacle 



(n, k, r_q, c_q, obstacles):


approach --

start the search from the point 

start the search in all direction 

with up, down , left , right , diagonal_left_up, diagonal_left_down, diagonal_right_up, diagonal_right_down

based on that traversaral will be done and base case elimination




"""




def helper_dfs(n,k,i,j,dir,obstacles,result):
	"""
	The function to make the helper dfs
	"""

	print("in")

	#base case 

	#if out of the bound 
	if i < 1 or j < 1 or i > n or j > n:

		return result

	#the obstacle case 
	if [i,j] in obstacles :

		dir = None


	#make the traverse in direction

	if dir == "up":

		print("up")

		helper_dfs(n,k,i-1,j,"up",obstacles, result + 1)

	if dir == "down":

		helper_dfs(n,k,i+1,j,"down",obstacles, result + 1)

	if dir == "left" :

		helper_dfs(n,k,i,j-1,"left",obstacles, result + 1)

	if dir == "right" :

		helper_dfs(n,k,i,j+1,"right",obstacles, result + 1)

	if dir == "diagonal_left_up" :

		helper_dfs(n,k,i-1,j-1,"diagonal_left_up",obstacles, result + 1)

	if dir == "diagonal_left_down" :

		helper_dfs(n,k,i-1,j+1,"diagonal_left_down",obstacles , result + 1)

	if dir == "diagonal_right_up" :

		helper_dfs(n,k,i+1,j-1,"diagonal_right_up",obstacles, result + 1)

	if dir == "diagonal_right_down" :

		helper_dfs(n,k,i+1,j+1,"diagonal_right_down",obstacles , result + 1)

	return result




def queensAttack(n,k,r_q,c_q,obstacles) :
	"""
	The function to find the number of attack can be made	
	"""


	#constraints case

	#make the recursion call
	up = helper_dfs(n,k,r_q,c_q,"up",obstacles,0)
	down = helper_dfs(n,k,r_q,c_q,"down",obstacles,0)
	left = helper_dfs(n,k,r_q,c_q,"left",obstacles,0)
	right = helper_dfs(n,k,r_q,c_q,"right",obstacles,0)
	diagonal_left_up = helper_dfs(n,k,r_q,c_q,"diagonal_left_up",obstacles,0)
	diagonal_left_down = helper_dfs(n,k,r_q,c_q,"diagonal_left_down",obstacles,0)
	diagonal_right_up = helper_dfs(n,k,r_q,c_q,"diagonal_right_up",obstacles,0)
	diagonal_right_down = helper_dfs(n,k,r_q,c_q,"diagonal_right_down",obstacles,0)

	return up + down + left + right + diagonal_left_down + diagonal_left_up + diagonal_right_up + diagonal_right_down




def queensAttack(n, k, r_q, c_q, obstacles):
    # Convert obstacles to a set for O(1) lookups
    obstacle_set = set((r, c) for r, c in obstacles)

    # Directions: (row_change, col_change)
    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1),   # right
        (-1, -1), # top-left
        (-1, 1),  # top-right
        (1, -1),  # bottom-left
        (1, 1)    # bottom-right
    ]

    total_attacks = 0

    # Iterate over each direction
    for dr, dc in directions:
        current_row, current_col = r_q, c_q

        # Move in the current direction until blocked or out of bounds
        while True:
            current_row += dr
            current_col += dc

            # Check if out of bounds
            if current_row < 1 or current_row > n or current_col < 1 or current_col > n:
                break

            # Check if square is blocked by an obstacle
            if (current_row, current_col) in obstacle_set:
                break

            # If not blocked, it's a valid square
            total_attacks += 1

    return total_attacks

















