"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
    If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

 
"""

"""
size fixed 

self.capacity = capacity 

get if exist -1 
    comes in head 

put if there update 
else : 
    add if less value
    capacity +=1 


mapper = {key : value_node} 







"""

class Node():

    def __init__(self,val= None,next = None):

        self.val = val
        self.next = next




class Linked_list_helper():

    def __init__(self):

        self.head = None
        self.tail = None


    def add_node(self,val):
        """
        The function to add node 
        """

        #make the node
        node = Node(val)

        #add the head 
        if not self.head:

            self.head = node
            self.tail = node

            return "Head is set "


        #add the tail 
        if not self.tail :

            self.tail = node 

            self.head.next = self.tail

            return "Tail is set"



        #add the node in middle 

        self.tail.next = node
        self.tail = node



        return "node is added"



    def list_printer(self):
        """
        The functon to print the list
        """

        if not self.head:
            return ""

        temp = self.head

        while temp:

            print(temp.val)
            temp = temp.next





class Node:

    def __init__(self,val = None,prev = None,next = None):

        self.val = val
        self.prev = prev
        self.next = next




class LRUCache:

    def __init__(self, capacity: int):
        """
        The function to set the initails of the LRU
        """
        self.capacity = capacity
        self.mapper = {}
        self.length = 0
        self.head = None
        self.tail = None



    def add_node(self,val):
        """
        The function to add the value in the doubly linked list 
        """

        #make the node 
        node = Node(val)


        if not self.head:

            self.head = node


        if not self.tail:

            self.tail = node
            
            #set the ptrs
            self.head.next = self.tail
            self.tail.prev = self.head




    def get(self, key: int) -> int:
        """
        The function to get the value of the key 
        """

        if key in self.mapper:

            #do the doubly linked list manupulation

            new_head = mapper[key]

            temp = mapper[key].prev
            temp2 = mapper[key].next

            temp.next = temp2
            temp2.prev = temp

            new_head.next = self.head
            new_head.prev = None

            self.head = new_head

            return mapper[key].val


        else:

            return -1 


        

    def put(self, key: int, value: int) -> None:
        """
        The fucntion to put the value in LRU 
        """

        #make the new node 
        node = Node(val)


        if key in self.mapper:

            #update the linke list 

            mapper[key].val = value

 


        #remove the least used 
        elif key not in self.mapper :

            pass




















