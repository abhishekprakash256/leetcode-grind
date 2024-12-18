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
graph[curr+1,min(curr + 6, n^2)]

curr = 1 

2 -- min(7,36)


how to know reach and can't reach 

if graph[i][j] == len(graph)*len(graph) :
	return False


#get the least number of moves ? 

range(curr+1 , min(curr + 6, n^2))

we can do a range of moves 

if the bfs return true then 

min_count = min(min_count,count)


 [[-1,-1,-1,-1,-1,-1],
 [-1,-1,-1,-1,-1,-1],
 [-1,-1,-1,-1,-1,-1],
 [-1,35,-1,-1,13,-1],
 [-1,-1,-1,-1,-1,-1], (1,1),(1,2)
 [-1,15,-1,-1,-1,-1]]


Output: 4

this is board 


how do I traverse the board in correct way 

take one row and reverse the other row and attach ? 

[-1,15,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,35,-1,-1,13,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]


make a list and revserse the row alternativley and append 


def make_linear_graph(board):
	
	graph_lst = []
	
	flip = True

	for row in boad :

		if flip :

			for i in row :

				graph_lst.append(i)

			flip = False

		else:
			
			row.reverse()
			for i in row :

				graph_lst.append(i)

			flip = True




"""




class Solution:

	def __init__(self):

		self.graph_lst = []
		self.move_lst = []



	def make_linear_graph(self,board):
		"""
		The function to make the graph linear
		"""
		
		flip = True

		for row in board :

			if flip :

				for i in row :

					self.graph_lst.append(i)

				flip = False

			else:
				
				row.reverse()

				for i in row :

					self.graph_lst.append(i)

				flip = True



	def graph_traversal(self,count, curr ):
		"""
		Make the traversal of the graph

		"""

		#make the base case 
		#starts with 0 for indexing but the number should be correct to -1

		if curr > len(self.board)*len(self.board) -1 :

			return False


		#make the move 
		for i in range(curr+1, min(curr + 6, len(self.board)*len(self.board))) :

			if curr > len(self.board)*len(self.board) -1 and len(self.move_lst) == 0:

				return False

			elif curr == len(self.board)*len(self.board) -1 :

				self.move_lst.append(count+1)

				return True

			elif self.board[curr] != -1:

				self.graph_traversal(count+1,self.board[curr]-1)

			else:

				self.graph_traversal(count+1,curr + i)


	




	def snakesAndLadders(self, board: List[List[int]]) -> int:
		"""
		The last value can be reached or not 
		"""

		self.board = board

		#base case 
		if len(self.board) == 1 :

			return 1

		#make the graph
		self.make_linear_graph(board)

		#iterate the graph from 0 
		self.graph_traversal(0,0)

		#count the min vales for moves 
		return self.move_lst.sort()[0]







