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


#correect solution
class Solution2:
    
    def helper(self, node, res_lst, level):
        if not node:
            return
        
        if level >= len(res_lst):
            res_lst.append([])
            
        if level % 2 == 0:
            res_lst[level].append(node.val)
        else:
            res_lst[level].insert(0, node.val)
        
        self.helper(node.left, res_lst, level + 1)
        self.helper(node.right, res_lst, level + 1)
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res_lst = []
        self.helper(root, res_lst, 0)
        return res_lst
        
        
        
