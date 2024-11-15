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

class Linkedlist():

    def __init__(self,val = None,next= None):

        self.val = val 
        self.next = next






class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.mapper = {}

        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key in self.mapper:

            return mapper[key]

            node = Node(mapper[key])

            node.next = head 

        else:

            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if self.key in mapper:


