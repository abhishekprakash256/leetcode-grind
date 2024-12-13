"""
The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagram:

A chess knight can move as indicated in the chess diagram below:
"""

"""
seems a graph question 

make the board 

[1,2,3]
[4,5,6]
[7,8,9]
[*,0,#]

I can do dfs and skip if hits * or # 
in the for loop cond 


traversal 


edge case 
very large return  modulo 10^9 + 7


number of jumps 

it's a dp question 

combines dfs and DP as well 







"""


grid = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
n = 1





class Solution:
	def knightDialer_graph(self, n: int) -> int:
		MOD = 10**9 + 7
		
		# Graph representation of the keypad
		graph = {
			0: [4, 6],
			1: [6, 8],
			2: [7, 9],
			3: [4, 8],
			4: [0, 3, 9],
			5: [],
			6: [0, 1, 7],
			7: [2, 6],
			8: [1, 3],
			9: [2, 4]
		}
		
		# Initialize DP table
		dp_prev = [1] * 10  # dp[1][j] = 1 for all j
		
		for i in range(2, n + 1):
			dp_curr = [0] * 10
			for j in range(10):
				for neighbor in graph[j]:
					dp_curr[j] += dp_prev[neighbor]
					dp_curr[j] %= MOD
			dp_prev = dp_curr  # Update for the next iteration
		
		# Total paths of length n
		return sum(dp_prev) % MOD


	# Python Implementation of Knight Dialer Problem

	def knightDialer(self,n):
		MOD = 10**9 + 7

		# Define possible moves for each key
		moves = {
			0: [4, 6],
			1: [6, 8],
			2: [7, 9],
			3: [4, 8],
			4: [0, 3, 9],
			5: [],
			6: [0, 1, 7],
			7: [2, 6],
			8: [1, 3],
			9: [2, 4]
		}

		# Base case: For length = 1, each key can form one number
		dp_prev = [1] * 10  # dp[1][j] = 1 for all j

		# Transition for lengths 2 to n
		for i in range(2, n + 1):
			dp_curr = [0] * 10
			for j in range(10):
				for neighbor in moves[j]:
					dp_curr[j] += dp_prev[neighbor]
					dp_curr[j] %= MOD  # Take modulo to avoid overflow
			dp_prev = dp_curr  # Update for the next iteration

		# Sum up all counts for numbers of length n
		return sum(dp_prev) % MOD



