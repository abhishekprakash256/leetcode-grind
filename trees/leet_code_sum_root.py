"""
leet code find the sum of the root ot leaf node
find the sum of the root node from the left and right 
we add and make a two digit number then we add them together 
Example 
-----

		8
	   / \
	  7   4

87 + 84 = 171
"""


"""
The methedelogy as follows - 


#base case 
if not node: 
	return 0 


#make the digit 

left_val = node.val* 10 + node.left.val 
right_val = node.val*10 + node.right.val

full sum 

node_sum = left_val + right_val





"""

