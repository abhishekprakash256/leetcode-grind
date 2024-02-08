"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

"""
constraints 

for two node always 

The algo -- 

def helper(self,node):

    return  node.val
    

def isValidBST(self,node):

    if node.left is None and node.right is None:
        return True

    left_val = self.helper(node.left) if node.left else return float('-inf')
    right_val = self.helper(node.right) if node.right else return float("inf")

    if left_val <= node.val <= right_val:
        return true

    else:
        return False



the node can be missing 

def helper(self,node):
    
    return node.val


def validBST(self,node):

    if node.left is None and node.right is None:
        return True

    left_val = self.helper(node.left) if node.left else float("-inf")
    right_val = self.helper(node.right) if node.right else float("-inf)


    if left_val < node.val < right_val:
        return True
    
    else:
        return False



---------------------------------------------------------------------------





algo --- 

#edge case 
if node.left is none and node.right is None:
    return True 


max_val = float("inf")
min_val = float("-inf") 


def helper(node):

    return node.val



def isValidBST(node):
    
    #base case
    if node.left is None and node.right is node:
        return True    

    left_val = self.helper(node.left) if node.left else float("-inf")
    right_val = self.helper(node.right) if node.right else float("inf")

    if left_val < node.val < right_val:
        
        return True 

    else:
        return True



















"""