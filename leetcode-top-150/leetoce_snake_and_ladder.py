"""
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.

"""



"""
move = [curr + 1, min(curr + 6, n^2)], it's a range 



snake or a ladder if board[r][c] != -1 


can't take the consequitive squares only one move at a time 

"""

"""
approach -- 

base case 

if graph[i][j] > len(graph)*len(graph) or graph[i][j] == -2:
	return None

visited marking with like -2 

node visted in queue and the pop and visiited again 

traversal techniques will be 
graph[curr+1][min(curr + 6, n^2)]

curr = 1 

2 -- min(7,36)

move can be in between 2 to 7 


how to know reach and can't reach 

if graph[i][j] == len(graph)*len(graph) :
	return False


#get the least number of moves ? 





"""




class Solution:

	def __init__(self):
		pass

	def graph_bfs(self,node):
		"""
		Make the bfs traversal of the graph

		"""
		pass


	def snakesAndLadders(self, board: List[List[int]]) -> int:
		"""
		The last value can be reached or not 
		"""
		pass