"""
Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.

Return the root of the Quad-Tree representing grid.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, 
each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. 
Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
isLeaf: True if the node is a leaf node on the tree or False if the node has four children.
class Node {
	public boolean val;
	public boolean isLeaf;
	public Node topLeft;
	public Node topRight;
	public Node bottomLeft;
	public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of 
the grid and set the four children to Null and stop.
If the current grid has different values, set isLeaf to False and set val to any value and divide the current
grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:

You don't need to read this section for solving the problem. This is only if you want to understand the output 
ormat here. The output represents the serialized format of a Quad-Tree using level order traversal, where null ignifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is 
represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of 
isLeaf or val is False we represent it as 0.
"""

"""

Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represents False and 1 represents True in the photo representing the Quad-Tree.


Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:


Constraints:

n == grid.length == grid[i].length
n == 2x where 0 <= x <= 6





"""


"""
approch -- 
first find all values same or not in a board 

then divide as per needed 

if all ones no divide 

if zeros we divide it into the quqd again 

islead = 1 
isVal = 1 or 0 depends on the values in the grid 

what we need -- 
some kind of searching and finding the mid point of the each grid 

recusive approach to find the grid like dfs and also the mid point finding 

and passing the values 

if is_val all are same then not divide 

else divide into the grid 

two type of recurins one for dfs search and other for making the node 

how find the mid 
(i+j) // 2

()






"""

"""
# Definition for a QuadTree node.
class Node:
	def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
		self.val = val
		self.isLeaf = isLeaf
		self.topLeft = topLeft
		self.topRight = topRight
		self.bottomLeft = bottomLeft
		self.bottomRight = bottomRight



"""


class Node:
	def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
		self.val = val
		self.isLeaf = isLeaf
		self.topLeft = topLeft
		self.topRight = topRight
		self.bottomLeft = bottomLeft
		self.bottomRight = bottomRight




class Solution1:
	def construct(self, grid: List[List[int]]) -> Node:
		return self.helper(grid, 0, 0, len(grid))


	def helper(self, grid, i, j, w):
		if self.allSame(grid, i, j, w):
			return Node(grid[i][j] == 1, True)

		node = Node(True, False)
		node.topLeft = self.helper(grid, i, j, w // 2)
		node.topRight = self.helper(grid, i, j + w // 2, w // 2)
		node.bottomLeft = self.helper(grid, i + w // 2, j, w // 2)
		node.bottomRight = self.helper(grid, i + w // 2, j + w // 2, w // 2)
		return node


	def allSame(self, grid, i, j, w):
		for x in range(i, i + w):
			for y in range(j, j + w):
				if grid[x][y] != grid[i][j]:
					return False
		return True





class Solution():
	def check_board(self,i,j,w):
		"""
		The funciton to check all board is same
		passes leetcode
		"""

		for a in range(i,i+w) :

			for b in range(j,j+w) :

				if self.board[a][b] != self.board[i][j] :
					return False

		return True



	def helper(self,i,j,w):
		"""
		The helper funcion for the traverdsal of the board 
		"""
		
		#base case
		if self.check_board(i,j,w):
			return Node(self.board[i][j] ,True)

		#make the leaves node
		node = Node(self.board[i][j], False)
		node.topLeft = self.helper(i, j, w // 2)
		node.topRight = self.helper(i, j + w // 2, w // 2)
		node.bottomLeft = self.helper( i + w // 2, j, w // 2)
		node.bottomRight = self.helper(i + w // 2, j + w // 2, w // 2)

		return node		





	def construct(self,board):
		"""
		The main function to call the recursive call
		"""
		self.board = board

		#make the recurseive call
		return self.helper(0,0,len(self.board))





























