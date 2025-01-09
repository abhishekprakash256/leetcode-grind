nums1 = [1,2,3,4,0,0,0]
nums2 = [2,5,6]



val = set()

val.add(4)

print(val)

print(len(" "))


"""

make the linked list
"""

class Node:
    def __init__(self,val=None,next = None ):
        self.val = val
        self.next = next



#make the node

head = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)

#connect the linked list 
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4


#print the list 

class Solution():

    def print_list(self,node):

        temp = node

        while temp:

            print(temp.val)

            temp = temp.next

    
    def rev_list(self,root):
        """
        The function to reverse the list 
        """

        #base case 
        if not root :
            return None


        #ptr 
        prev = None
        curr = root

        #start the loop 
        while curr:

            temp = prev 
            prev = curr
            curr = curr.next
            prev.next = temp
        
        return prev

        








sol = Solution()
print(sol.print_list(head))
sol.rev_list(head)
print(sol.print_list(node4))



my_dict = {'a': 1, 'b': 2, 'c': 3}

del my_dict['b']  # Removes the key-value pair with key 'b'

my_dict.pop("c")

print(my_dict)


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

print(len(triangle))

print(len(triangle[1]))

print(triangle[3])