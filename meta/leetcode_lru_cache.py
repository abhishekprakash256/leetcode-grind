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



make a doubly linked list and use head and tail for the swap 

head most recntly used 

tail least used 

use a mapper for keeping the values

mapper = {2 : 0 , 1 : 1 }


[2,1]

"""



class LRUCache:

    def __init__(self, capacity: int):
    	self.mapper = {}
    	self.capacity = capacity
    	self.lst = []

        

    def get(self, key: int) -> int:
    	"""
		The function to pass to get the key value 
    	"""

    	#check if the value in mapper :

    	if key in self.mapper :

    		temp_idx = self.mapper[key]
    		temp_val = self.lst[self.mapper[key]]

    		#update the head 
    		self.lst[0] , self.lst[self.mapper[key]] = self.lst[self.mapper[key]] , self.lst[0]

    		#update the dict value
    		self.mapper[key] = 0 
    		self.mapper[]
        

    def put(self, key: int, value: int) -> None:
    	"""
		The function to update the key value or put the key value if exists 
    	"""

