"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, 
add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation,
vict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""


"""
approach


class LRUCache:

    def __init__(self, capacity: int):
        

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:



mapper has the key and indx of the val in the list 

doubly linked list approach 

TreeNode
prev and next 

LinkedList 
head and tail 

swap the head and tail 

update the hash map ? 










"""

class Node():
    def __init__(self,key , value, prev = None, next = None) :

        self.value = value
        self.key = key
        self.prev = prev
        self.next = next




class LRUCache:
    """
    passes leet code
    """

    def __init__(self, capacity: int):
        self.mapper = {}
        self.capacity = capacity
        self.head = Node(None,None)  # Dummy head (most recently used)
        self.tail = Node(None,None)  # Dummy tail (least recently used)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self,node):
        """
        The function to remove the node
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _set_after_head(self,node) :
        """
        The function to set the head 
        """
        temp_node = self.head.next
        node.prev = self.head
        node.next = temp_node
        temp_node.prev = node
        self.head.next = node
        


    def get(self, key: int) -> int:
        """
        The function to pass to get the key value 
        """
        
        #if the key exists in the mapper 
        if key in self.mapper:
           
            node = self.mapper[key]
            # Move the accessed node to the head (most recently used)
            self._remove_node(node)
            self._set_after_head(node)
            return node.value
        

        return -1



    def put(self, key: int, value: int) -> None:
        """
        The function to update the key value or put the key value if exists 
        """
        
        if key in self.mapper:
            # Update the value and move node to head
            node = self.mapper[key]
            node.value = value
            self._remove_node(node)
            self._set_after_head(node)

        else:
            # Add a new node
            if len(self.mapper) == self.capacity:
                # Evict the least recently used node
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.mapper[lru_node.key]
                
            new_node = Node(key, value)
            self._set_after_head(new_node)
            self.mapper[key] = new_node       

