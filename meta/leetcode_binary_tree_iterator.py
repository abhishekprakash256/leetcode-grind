"""
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
"""



"""


Constraints:

The number of nodes in the tree is in the range [1, 105].
0 <= Node.val <= 106
At most 105 calls will be made to hasNext, and next.
 

Follow up:

Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?

"""


"""
approach -- 

using a dfs traversal , left , root , right

use a dfs fucnton with res to craete a list array and append the elements 

the interate the list 


"""





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):

        self.root = root
        self.result = []
        self.i = 0
        self._dfs_iter(self.root)


    def _dfs_iter(self,node):
        """
        The function to make the dfs iter for the tree
        """

        #make the iter 

        #base case 
        if node :
            
            if node.left :
                
                self._dfs_iter(node.left)

            self.result.append(node.val)


            if node.right :

                self._dfs_iter(node.right)


        

    def next(self) -> int:
        """
        The function to get the next value 
        """

        temp = self.i 

        self.i += 1 

        return self.result[temp]




    def hasNext(self) -> bool:
        """
        The function to check the next value exist or not 
        """

        if self.i <= len(self.result) - 1 :

            return self.result[self.i]

        return False