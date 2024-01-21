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

		4
	   / \
	  9   0
	 / \
	5   1


495 + 491 = 1026


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


two function , using recursion --- 


def helper()




def sumNumbers(self,root)





"""

