# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#wrong code ---------------------------------------------------
class Solution:
    
    def helper(self,node,res_lst,flip,tempr_lst= []):
        """
        The helper function for traversal
        """
        if not node:
            tempr_lst = []
            return None
        
        
        if flip is True:
            
            tempr_lst.append(node.val)
            self.helper(node.left,res_lst,flip,tempr_lst)
            self.helper(node.right,res_lst,flip,tempr_lst)
            res_lst.append(tempr_lst)
            flip = False
            
            
        else:
            
            tempr_lst.append(node.val)
            self.helper(node.right,res_lst,flip,tempr_lst)
            self.helper(node.left,res_lst,flip,tempr_lst)
            res_lst.append(tempr_lst)
            flip = True
            
            
        

            
    
    def zigzagLevelOrder(self, node: Optional[TreeNode]) -> List[List[int]]:
        
        res_lst = []
        flip = True
        
        if not node:
            return None
        
        self.helper(node,res_lst,flip)
        
        return res_lst
        
        
        
        
