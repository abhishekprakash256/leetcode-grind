"""
the function to find the tree are same 

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value.
"""


"""
Input: p = [1,2,3], q = [1,2,3]
Output: true


"""


"""
approach 

traversal problem 

def traverse(self,node):

    if not node:
        return None
    
    self.traverse(node.left)
    self.traverse(node.right)

    return node.val


        
def main(self,node):   

    #base case 
    if not node :
     
        return None

    left = self.traverse(node.left)
    right = self.traverse(node.right)

    if left == right :
        return True
    
    else:
        
        return False


"""

class Solution:

    def traverse(self,node):
        """
        The traverse function 
        """

        if not node :
            return None
    

        return node.val

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        The main checking function
        """

        #base case 
        if not q or not p:
            
            return False
        
        if p.left and q.left:

            p_left = self.traverse(p.left)
            q_right = self.traverse(q.left)
        
        if p.right and q.right : 

            p_right = self.traverse(p.right)
            q_right = self.traverse(q.right)
        

        


         

