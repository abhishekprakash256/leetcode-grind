"""
find the number of unique paths in the grid from left most to point to right most down point 
"""

def find_path(n,m):
	"""
	The function fins the solution using recursion 
	as base case is one grid
	"""

	if n == 1 or m == 1:
		return 1 

	else:
		return find_path(n-1,m) + find_path(n,m-1)
