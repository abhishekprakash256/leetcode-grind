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




class LRUCache_wrong:

    def __init__(self, capacity: int):
        """
        The function to set the initails of the LRU
        """
        self.capacity = capacity
        self.mapper = {}
        self.length = 0
        self.head = None  #the recently used
        self.tail = None  #tail the lastly used


        

    def get(self, key: int) -> int:
        """
        The functon to get the value of the key value and set it to head
        """
        
        if key in self.mapper:

            #put the node in head
            #if node is head 

            if self.mapper[key] == self.head:

                return self.mapper[key].val

            #if node is not head 
            elif self.mapper[key] == self.tail :

                temp_node = self.tail.prev 

                self.tail.next = self.head
                self.head.prev = self.tail 

                self.tail.prev = None
                self.head = self.tail

                temp_node.next = None

                self.tail = temp_node

                return self.mapper[key].val

            #if node not head or tail
            else:

                temp_prev = self.mapper[key].prev
                temp_next = self.mapper[key].next

                temp_prev.next = temp_next
                temp_next.prev = temp_prev

                self.head.prev = self.mapper[key]
                self.mapper[key].next = self.head

                self.head = self.mapper[key]
             

                return self.mapper[key].val
    
        else:

            return -1 
        

    def put(self, key: int, value: int) -> None:
        """
        The function to put the value only if capacity is length
        """

        #update the value if present

        if key in self.mapper : 

            self.mapper[key].val = value

        
        #if the value is not present and length is less than capacity

        if key not in self.mapper and self.length != self.capacity : 

            node = Node(value)
            self.length += 1 

            #if head is not set

            if not self.head: 

                self.head = node

                self.tail = node

            #if tail is not set

            elif not self.tail: 

                self.node.prev = self.head

                self.head.next = node

                self.tail = node
            

            #if other node is not set

            else:

                node.prev = self.tail

                self.tail.next = node

                self.tail = node
                
            self.mapper[key] = node

        
        if key in self.mapper and self.length == self.capacity : 
            
            #cut the tail and put new value in mapper 

            node = Node(value)

            #remove the value from mapper 
            self.mapper.pop(key)

            #remove the tail 

            temp_node = self.tail.prev

            temp_node.next = node
            node.prev = temp_node

            self.tail.prev = None

            self.tail = node





class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with a fixed capacity.
        passes leetcode
        """
        self.capacity = capacity
        self.mapper = {}  # Dictionary for O(1) access to nodes
        self.head = Node()  # Dummy head (most recently used)
        self.tail = Node()  # Dummy tail (least recently used)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """
        Remove a node from the doubly linked list.
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: Node):
        """
        Add a node right after the dummy head.
        """
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        """
        Return the value of the key if it exists in the cache, otherwise return -1.
        """
        if key in self.mapper:
            node = self.mapper[key]
            # Move the accessed node to the head (most recently used)
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Add a key-value pair to the cache. If the cache exceeds capacity, evict the least recently used item.
        """
        if key in self.mapper:
            # Update the value and move node to head
            node = self.mapper[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            # Add a new node
            if len(self.mapper) == self.capacity:
                # Evict the least recently used node
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.mapper[lru_node.key]
            new_node = Node(key, value)
            self._add_to_head(new_node)
            self.mapper[key] = new_node























