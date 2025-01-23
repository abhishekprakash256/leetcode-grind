"""
make the square the magic square at the cost of chnage in elements

We define a magic square to be an  matrix of distinct positive integers from  to  where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.

You will be given a  matrix  of integers in the inclusive range . We can convert 
any digit  to any other digit  in the range  at cost of . Given , convert it into a magic square at 
minimal cost. Print this cost on a new line.

Note: The resulting magic square must contain distinct integers in the inclusive range .
"""

"""

$s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

The matrix looks like this:


5 3 4 + 3 
1 5 8 + 1
6 4 2 + 1

We can convert it to the following magic square:

8 3 4
1 5 9
6 7 2

This took three replacements at a cost of . 7 

The matrix is 3X3 

we can take the sum - 

5+3+4 = 12 
1+5+8 = 14 
6+4+2 = 12

5+1+6 =12
3+5+4=12
4+8+2 = 14


5 + 5 + 2 = 12
4 + 5 + 6 = 15

min val ? 

chage the sum to 15 







"""


def formingMagicSquare(S):
	"""
	passes the code
	"""
    # All 8 possible magic squares
    magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]
    
    min_cost = float('inf')
    
    # Compare S with each magic square
    for magic in magic_squares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(S[i][j] - magic[i][j])
        min_cost = min(min_cost, cost)
    
    return min_cost

# Example Usage
S = [
    [4, 8, 7],
    [3, 9, 5],
    [1, 2, 6]
]
print(formingMagicSquare(S))  # Output the minimal cost
